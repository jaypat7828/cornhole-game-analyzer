# download_model.py
import os
import shutil
from ultralytics import YOLO

# Download the model (saved locally in cwd)
print("Downloading YOLOv8n model...")
model = YOLO("yolov8n.pt")  # This triggers download to ./yolov8n.pt if not found

# Define source and destination
source_path = "yolov8n.pt"
target_dir = "models"
target_path = os.path.join(target_dir, "yolov8n.pt")

# Ensure target folder exists
os.makedirs(target_dir, exist_ok=True)

# Move the model to models folder
if os.path.exists(source_path):
    shutil.move(source_path, target_path)
    print(f"Model successfully moved to {target_path}")
else:
    print("Error: Model not found after download.")