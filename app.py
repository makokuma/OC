import streamlit as st
import subprocess
from pathlib import Path

st.title("昔の天気を見てみよう")

png_path = Path("enshu1_rainarea.png")

if st.button("描画する"):
    # 前回の画像が残っていると紛らわしいので消す
    if png_path.exists():
        png_path.unlink()

    command = [
        "grads",
        "-blc",
        "run enshu_1.gs"
    ]

    with st.spinner("描画中..."):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )

    if result.returncode == 0 and png_path.exists():
        st.success("描画できました")
        st.image(str(png_path))
    else:
        st.error("描画に失敗しました")
        st.write("stdout")
        st.code(result.stdout)
        st.write("stderr")
        st.code(result.stderr)
