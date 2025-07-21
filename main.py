from tracker import track_players_and_bags
from scorer import calculate_score_and_annotate
from utils import save_annotated_video
import cv2

def process_video(input_path):
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps is None:
        fps = 30  # fallback FPS

    cap.release()

    # Call YOLO tracking
    results = track_players_and_bags(input_path)

    # Check if results is a list of Results objects
    frames = []
    try:
        for result in results:
            if hasattr(result, "plot"):
                frames.append(result.plot())
            else:
                print("Warning: result object does not have .plot method")
    except Exception as e:
        print(f"Error while extracting frames from results: {e}")
        frames = []

    print(f"Total frames before annotation: {len(frames)}")

    # Safety: only proceed if we have frames
    if not frames:
        raise RuntimeError("No frames were extracted from tracking results.")

    # Optional: annotate + score (placeholder for now)
    annotated_frames = calculate_score_and_annotate(frames)
    print(f"Total frames after annotation: {len(annotated_frames)}")

    return save_annotated_video(annotated_frames, fps)
