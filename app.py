import streamlit as st
from main import process_video

st.title("Cornhole Game Analyzer")

video_file = st.file_uploader("Upload Cornhole Game Video", type=["mp4", "mov"])

if video_file is not None:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(video_file.read())
    st.video("uploaded_video.mp4")
    if st.button("Analyze Game"):
        output_path = process_video("uploaded_video.mp4")
        st.video(output_path)
        st.success("Analysis complete!")