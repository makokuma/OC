import streamlit as st
import subprocess
from pathlib import Path
import uuid

st.title("昔の天気を見てみよう")


job_id = uuid.uuid4().hex
print(job_id)
APP_DIR = Path(__file__).resolve().parent
png_path = APP_DIR / f"enshu1_rainarea_{job_id}.png"

if st.button("描画する"):
    # 前回の画像が残っていると紛らわしいので消す
    if png_path.exists():
        png_path.unlink()
    #assign job id
    job_id = uuid.uuid4().hex
    print(job_id)
    APP_DIR = Path(__file__).resolve().parent
    png_path = APP_DIR / f"enshu1_rainarea_{job_id}.png"

    command = [
        "grads",
        "-blc",
        f"run enshu_1.gs {png_path}"
    ]

    with st.spinner("描画中..."):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )

    st.subheader("実行結果")
    st.write("returncode:", result.returncode)
    st.write("PNG path:", str(png_path))
    st.write("PNG exists:", png_path.exists())

    if png_path.exists():
        st.write("PNG size:", png_path.stat().st_size)

    with st.expander("実行ログを見る", expanded=True):
        st.write("実行コマンド")
        st.code(" ".join(command))

        st.write("stdout")
        st.code(result.stdout or "(stdoutなし)")

        st.write("stderr")
        st.code(result.stderr or "(stderrなし)")

    if png_path.exists(): #do not use result.returncode == 0
        st.success("描画できました")
        st.image(str(png_path))
    else:
        st.error("描画に失敗しました")
        st.write("stdout")
        st.code(result.stdout)
        st.write("stderr")
        st.code(result.stderr)
