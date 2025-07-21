import cv2

def calculate_score_and_annotate(frames):
    for i, frame in enumerate(frames):
        cv2.putText(frame, f"Frame: {i+1}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    return frames
