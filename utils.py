def save_annotated_video(frames, fps, output_path="outputs/output.mp4"):
    import os
    import cv2

    if not frames:
        print("❌ No frames to write.")
        return output_path

    h, w, _ = frames[0].shape
    w, h = int(w), int(h)

    if fps == 0 or fps is None:
        fps = 30

    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    for f in frames:
        out.write(f)
    out.release()
    print(f"✅ Video saved successfully: {output_path}")
    return output_path
