import streamlit as st
import subprocess
from pathlib import Path
import uuid

st.title("昔の天気を見てみよう")

png_path = Path("enshu1_rainarea.png")

if st.button("描画する"):
    # 前回の画像が残っていると紛らわしいので消す
    if png_path.exists():
        png_path.unlink()
    #assign job id
    job_id = uuid.uuid4().hex
    png_path = Path(f"enshu1_rainarea_{job_id}.png")

    command = [
        "grads",
        "-blc",
        "run enshu_1.gs {png_path}"
    ]

    with st.spinner("描画中..."):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )

    if png_path.exists(): #do not use result.returncode == 0
        st.success("描画できました")
        st.image(str(png_path))
    else:
        st.error("描画に失敗しました")
        st.write("stdout")
        st.code(result.stdout)
        st.write("stderr")
        st.code(result.stderr)
