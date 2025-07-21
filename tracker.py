from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

def track_players_and_bags(video_path):
    results = model.track(video_path, persist=True)
    print(f"Tracking done. Results type: {type(results)}, Length: {len(results) if isinstance(results, list) else 'N/A'}")
    return results
