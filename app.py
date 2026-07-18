#display at streamlit
import streamlit as st
import subprocess
from pathlib import Path
import uuid
from datetime import date


from time_util import grads_time
from path_util import get_ctl_path
from config import PLOT_CONFIG
from grads_runner import run_grads

APP_DIR = Path(__file__).resolve().parent
GS_DIR = APP_DIR / "gs"
OUTPUT_DIR = APP_DIR / "output"

PLOT_GS = GS_DIR / "plot_map.gs"

OUTPUT_DIR.mkdir(exist_ok=True)

st.set_page_config(
    page_title="RRJ-Conv描画ツール",
    layout="wide",
)

st.title("RRJ-Conv描画ツール")
st.write("任意の日付、要素を選択してください")

#input
selected_date = st.date_input(
        "日付",
        value=date(2020, 7, 4),
        )

hour = st.selectbox(
    "時刻",
    ["0", "3", "6", "9", "12", "15", "18", "21"],
    index=3,
)
hour = int(hour)

plot_labels = {
    config["label"]: key
    for key, config in PLOT_CONFIG.items()
}

plot_label = st.selectbox(
    "表示する図",
    list(plot_labels.keys()),
)

plot_key = plot_labels[plot_label]
plot_config = PLOT_CONFIG[plot_key]

#for grads
gtime = grads_time(selected_date.year, selected_date.month, selected_date.day, hour)
ctl_path = get_ctl_path(selected_date.year, selected_date.month, plot_config["ctrl_grp"])

job_id = uuid.uuid4().hex
png_path = OUTPUT_DIR / f"{plot_key}_{selected_date:%Y%m%d}_{hour}_{job_id}.png"

# debug
with st.expander("現在の設定", expanded=False):
    st.write("plot_key:", plot_key)
    st.write("grads_time:", gtime)
    st.write("ctl_path:", str(ctl_path))
    st.write("output:", str(png_path))

#execute
if st.button("描画する", type="primary"):
    # plot_map.gs の引数順: ctlpath, gtime, varname, gxout, lat1, lat2, lon1, lon2, outpng
    args = [
        ctl_path,
        gtime,
        plot_config["grads_var"],
        plot_config["gxout"],
        plot_config["lat_range"][0],
        plot_config["lat_range"][1],
        plot_config["lon_range"][0],
        plot_config["lon_range"][1],
        png_path,
    ]

    with st.spinner("描画中..."):
        command, result = run_grads(
            gs_path=PLOT_GS,
            args=args,
            timeout=60,
        )

    png_ok = png_path.exists() and png_path.stat().st_size > 0

    if png_ok:
        st.success("描画できました")
        st.image(str(png_path), caption=f"{selected_date} {hour}時：{plot_label}")
    else:
        st.error("PNGが作成されませんでした")

    with st.expander("実行ログを見る", expanded=not png_ok):
        st.write("実行コマンド")
        st.code(" ".join(command))

        st.write("returncode:", result.returncode)

        st.write("stdout")
        st.code(result.stdout or "(stdoutなし)")

        st.write("stderr")
        st.code(result.stderr or "(stderrなし)")
