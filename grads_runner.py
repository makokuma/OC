#open grads settings
import subprocess

def run_grads(gs_path, args, timeout=60):
    command = ["grads", "-blc", f"run {gs_path} {' '.join(map(str, args))}"]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout
    )
    return command, result
