#display at streamlit
import streamlit as st
import subprocess
from pathlib import Path
import uuid
from datetime import date


from time_util import grads_time, grads_time_from_jst
from path_util import get_ctl_path
from config import PLOT_CONFIG, EVENT_CONFIG, REGION_CONFIG
from grads_runner import run_grads

APP_DIR = Path(__file__).resolve().parent
GS_DIR = APP_DIR / "gs"
OUTPUT_DIR = APP_DIR / "output"

PLOT_GS = GS_DIR / "plot_map.gs"
COLORS_GS = GS_DIR / "color_bar.gs"

OUTPUT_DIR.mkdir(exist_ok=True)

st.set_page_config(
    page_title="RRJ-Conv描画ツール",
    layout="wide",
)

st.title("RRJ-Conv描画ツール")

plot_labels = {
    config["label"]: key
    for key, config in PLOT_CONFIG.items()
}

event_labels = {
    event["label"]: key
    for key, event in EVENT_CONFIG.items()
}

region_labels = {
    region["label"]: key
    for key, region in REGION_CONFIG.items()
}


#plot_map.gs の引数順: ctlpath, gtime, varname, gxout, lat1, lat2, lon1, lon2, outpng
def draw(selected_date, hour, plot_key, plot_label, lat_range, lon_range, key_prefix):
    plot_config = PLOT_CONFIG[plot_key]

    gtime = grads_time_from_jst(
        selected_date.year,
        selected_date.month,
        selected_date.day,
        hour,
    )
    #gtime = grads_time(selected_date.year, selected_date.month, selected_date.day, hour)
    ctl_path = get_ctl_path(selected_date.year, selected_date.month, plot_config["ctrl_grp"])

    job_id = uuid.uuid4().hex
    png_path = OUTPUT_DIR / f"{plot_key}_{selected_date:%Y%m%d}_{hour}_{job_id}.png"

    with st.expander("現在の設定", expanded=False):
        st.write("plot_key:", plot_key)
        st.write("grads_time:", gtime)
        st.write("ctl_path:", str(ctl_path))
        st.write("output:", str(png_path))

    if st.button("描画する", type="primary", key=f"{key_prefix}_run"):
        args = [
            ctl_path,
            gtime,
            plot_key,
            plot_config["grads_var"],
            plot_config["gxout"],
            lat_range[0],
            lat_range[1],
            lon_range[0],
            lon_range[1],
            COLORS_GS,
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

#another tub 1
tab_free, tab_event = st.tabs(["自由に選ぶ", "おすすめの日"])

#default tub select
with tab_free:
    st.write("任意の日付、要素を選択してください")

    selected_date = st.date_input(
        "日付",
        value=date(2020, 7, 4),
        key="free_date",
    )

    hour = st.selectbox(
        "時刻(JST)",
        ["0", "3", "6", "9", "12", "15", "18", "21"],
        index=3,
        key="free_hour",
    )
    hour = int(hour)

    plot_label = st.selectbox(
        "表示する図",
        list(plot_labels.keys()),
        key="free_plot",
    )
    plot_key = plot_labels[plot_label]
    plot_config = PLOT_CONFIG[plot_key]

    region_label = st.selectbox(
        "表示領域",
        list(region_labels.keys()),
        key="free_region",
    )
    region_config = REGION_CONFIG[region_labels[region_label]]

    draw(
        selected_date, hour, plot_key, plot_label,
        region_config["lat_range"], region_config["lon_range"],
        key_prefix="free",
    )

#another tub 1
with tab_event:
    st.write("おすすめの事例から選んでください")

    selected_event_label = st.selectbox(
        "おすすめ事例",
        list(event_labels.keys()),
        key="event_select",
    )
    event = EVENT_CONFIG[event_labels[selected_event_label]]
    st.caption(event["description"])

    event_date = date(*event["date"])

    draw(
        event_date, event["hour"], event["plot_key"], PLOT_CONFIG[event["plot_key"]]["label"],
        event["lat_range"], event["lon_range"],
        key_prefix="event",
    )
