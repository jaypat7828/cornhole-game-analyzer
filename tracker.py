from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

def track_players_and_bags(video_path):
    results = model.track(video_path, persist=True)
    return results