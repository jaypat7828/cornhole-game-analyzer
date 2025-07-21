import streamlit as st
from main import process_video
import os

st.set_page_config(page_title="Cornhole Game Analyzer", layout="centered")
st.title("🎯 Cornhole Game Analyzer")

uploaded_file = st.file_uploader("Upload a Cornhole Game Video", type=["mp4"])

if uploaded_file:
    temp_input_path = "uploaded_video.mp4"
    
    # Save uploaded file
    with open(temp_input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.subheader("▶ Original Video")
    st.video(temp_input_path)

    if st.button("🔍 Analyze Video"):
        with st.spinner("Running YOLO tracking and scoring..."):
            output_path = process_video(temp_input_path)
        st.success("✅ Analysis Complete!")

        print("File exists?", os.path.exists(output_path))

        st.subheader("🏁 Annotated Output")
        if os.path.exists(output_path):
            st.video(output_path)
        else:
            st.error("Output video not found. Check processing pipeline.")
