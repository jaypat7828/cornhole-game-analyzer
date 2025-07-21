import cv2
import os

def save_annotated_video(frames, fps, output_path="output.mp4"):
    if not frames:
        return output_path
    h, w, _ = frames[0].shape
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
    for f in frames:
        out.write(f)
    out.release()
    return output_path