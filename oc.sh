# ~/.config/oc/oc.sh

_oc_load_client_config() {
  if [ ! -f "$_OC_CLIENT_CONFIG" ]; then
    echo "OC client configuration was not found:" >&2
    echo "  $_OC_CLIENT_CONFIG" >&2
    return 1
  fi

  # shellcheck source=/dev/null
  source "$_OC_CLIENT_CONFIG"
}

_OC_CLIENT_CONFIG="${OC_CLIENT_CONFIG:-$HOME/.config/oc/client.conf}"


_oc_validate_client_config() {
  local name
  local value

  for name in \
    OC_HOST \
    OC_PORT \
    OC_SERVER_ALIVE_INTERVAL \
    OC_SERVER_ALIVE_COUNT_MAX \
    OC_CONTROL_DIR \
    OC_CONTROL_SOCKET
  do
    eval "value=\${${name}:-}"

    if [ -z "$value" ]; then
      echo "OC configuration error: ${name} is not set." >&2
      return 1
    fi
  done
}

_oc_is_wsl() {
  if [ -r /proc/version ] &&
     grep -qi microsoft /proc/version 2>/dev/null
  then
    return 0
  fi

  if [ -r /proc/sys/kernel/osrelease ] &&
     grep -qi microsoft /proc/sys/kernel/osrelease 2>/dev/null
  then
    return 0
  fi

  return 1
}


_oc_open_browser() {
  local url="$1"

  if _oc_is_wsl; then
    cmd.exe /c start "" "$url" >/dev/null 2>&1
    return $?
  fi

  case "$(uname -s)" in
    Darwin)
      open "$url"
      ;;

    Linux)
      if command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$url" >/dev/null 2>&1
      elif command -v gio >/dev/null 2>&1; then
        gio open "$url" >/dev/null 2>&1
      else
        echo "Could not open the browser automatically."
        echo "Open this URL manually:"
        echo "  $url"
      fi
      ;;

    *)
      echo "Could not identify the browser command."
      echo "Open this URL manually:"
      echo "  $url"
      ;;
  esac
}


_oc_master_running() {
  [ -S "$OC_CONTROL_SOCKET" ] &&
    ssh \
      -S "$OC_CONTROL_SOCKET" \
      -O check \
      "$OC_HOST" \
      >/dev/null 2>&1
}


_oc_close_master() {
  if _oc_master_running; then
    ssh \
      -S "$OC_CONTROL_SOCKET" \
      -O exit \
      "$OC_HOST" \
      >/dev/null 2>&1 || true
  fi

  rm -f "$OC_CONTROL_SOCKET"
}


_oc_check_required_commands() {
  local command_name

  for command_name in ssh curl uname; do
    if ! command -v "$command_name" >/dev/null 2>&1; then
      echo "Required command was not found: $command_name" >&2
      return 1
    fi
  done
}


oc() {
  _oc_load_client_config || return 1
  _oc_validate_client_config || return 1
  _oc_check_required_commands || return 1

  local url="http://localhost:${OC_PORT}"

  mkdir -p "$OC_CONTROL_DIR" || return 1
  chmod 700 "$OC_CONTROL_DIR"

  echo "Stopping old OC SSH tunnel..."
  _oc_close_master

  echo "Starting SSH tunnel..."
  echo "SSH authentication should normally be requested once."

  ssh \
    -M \
    -S "$OC_CONTROL_SOCKET" \
    -fN \
    -L "127.0.0.1:${OC_PORT}:127.0.0.1:${OC_PORT}" \
    -o ExitOnForwardFailure=yes \
    -o ServerAliveInterval="$OC_SERVER_ALIVE_INTERVAL" \
    -o ServerAliveCountMax="$OC_SERVER_ALIVE_COUNT_MAX" \
    "$OC_HOST"

  if [ "$?" -ne 0 ]; then
    echo "SSH tunnel could not be started." >&2
    rm -f "$OC_CONTROL_SOCKET"
    return 1
  fi

  echo "Checking SSH tunnel..."

  if ! _oc_master_running; then
    echo "SSH ControlMaster connection is not running." >&2
    rm -f "$OC_CONTROL_SOCKET"
    return 1
  fi

  echo "Starting remote Streamlit..."

  ssh \
    -S "$OC_CONTROL_SOCKET" \
    "$OC_HOST" \
    bash --noprofile --norc -s -- "$OC_PORT" <<'REMOTE_SCRIPT'

PORT=$1
SERVER_CONFIG="$HOME/.config/oc/server.conf"

if [ ! -f "$SERVER_CONFIG" ]; then
  echo "OC server configuration was not found:" >&2
  echo "  $SERVER_CONFIG" >&2
  exit 20
fi

# shellcheck source=/dev/null
source "$SERVER_CONFIG"

for name in OC_APP_DIR OC_VENV_BIN OC_LOG_FILE OC_DATA_ROOT; do
  eval "value=\${$name:-}"

  if [ -z "$value" ]; then
    echo "OC server configuration error: ${name} is not set." >&2
    exit 21
  fi
done

cd "$OC_APP_DIR" || exit 12

pkill -f "[s]treamlit run app.py.*--server.port[ =]${PORT}" \
  2>/dev/null || true

sleep 1
rm -f "$OC_LOG_FILE"

export OC_DATA_ROOT

nohup "${OC_VENV_BIN}/python" -m streamlit run app.py \
  --server.address 127.0.0.1 \
  --server.port "$PORT" \
  --server.headless true \
  >"$OC_LOG_FILE" 2>&1 </dev/null &

REMOTE_SCRIPT

  if [ "$?" -ne 0 ]; then
    echo "Remote Streamlit could not be started." >&2
    _oc_close_master
    return 1
  fi

  echo "Waiting for Streamlit..."

  local app_ready=0
  local i=1

  while [ "$i" -le 30 ]; do
    if curl -fsS \
      "http://127.0.0.1:${OC_PORT}/_stcore/health" \
      >/dev/null 2>&1
    then
      app_ready=1
      break
    fi

    printf "."
    sleep 1
    i=$((i + 1))
  done

  echo

  if [ "$app_ready" -ne 1 ]; then
    echo "Streamlit could not be reached through the tunnel." >&2
    echo
    echo "Check the remote log with:"
    echo "  ssh ${OC_HOST} 'source ~/.config/oc/server.conf && tail -n 50 \"\$OC_LOG_FILE\"'"
    return 1
  fi

  echo "Streamlit is ready."
  echo "Opening browser..."

  _oc_open_browser "$url"

  echo "Streamlit URL: $url"
}


oc_stop() {
  _oc_load_client_config || return 1
  _oc_validate_client_config || return 1

  echo "Stopping OC SSH tunnel..."

  if _oc_master_running; then
    _oc_close_master
    echo "OC tunnel stopped."
  else
    rm -f "$OC_CONTROL_SOCKET"
    echo "No OC tunnel is running."
  fi
}


oc_status() {
  _oc_load_client_config || return 1
  _oc_validate_client_config || return 1

  local url="http://localhost:${OC_PORT}"

  if _oc_master_running; then
    echo "OC tunnel is running."
    echo "URL: $url"

    if curl -fsS \
      "http://127.0.0.1:${OC_PORT}/_stcore/health" \
      >/dev/null 2>&1
    then
      echo "Streamlit is responding."
    else
      echo "The tunnel is running, but Streamlit is not responding."
    fi
  else
    echo "OC tunnel is not running."
  fi
}


oc_log() {
  _oc_load_client_config || return 1
  _oc_validate_client_config || return 1

  ssh "$OC_HOST" '
    SERVER_CONFIG="$HOME/.config/oc/server.conf"

    if [ ! -f "$SERVER_CONFIG" ]; then
      echo "Server configuration not found: $SERVER_CONFIG" >&2
      exit 1
    fi

    source "$SERVER_CONFIG"
    tail -n 50 "$OC_LOG_FILE"
  '
}


# 従来のコマンド名も残す
alias oc-stop='oc_stop'
alias oc-status='oc_status'
alias oc-log='oc_log'
