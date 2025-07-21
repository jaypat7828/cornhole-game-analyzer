from ultralytics import YOLO
import os

model = YOLO("models/yolov8n.pt")

def write_detected_objects_to_file(results):
    """
    Extract unique detected objects from YOLO results and write them to detected_objects.txt
    """
    unique_objects = set()
    
    # Extract unique object names from results
    for result in results:
        if hasattr(result, 'names') and result.names:
            # Get detected object names from this frame
            if hasattr(result, 'boxes') and result.boxes is not None:
                for box in result.boxes:
                    if hasattr(box, 'cls') and box.cls is not None:
                        for cls_id in box.cls:
                            if cls_id < len(result.names):
                                object_name = result.names[int(cls_id)]
                                unique_objects.add(object_name)
    
    # Write unique objects to file
    if unique_objects:
        with open('detected_objects.txt', 'w') as f:
            for obj in sorted(unique_objects):
                f.write(f"{obj}\n")
        print(f"✅ Unique detected objects written to detected_objects.txt: {sorted(unique_objects)}")
    else:
        print("⚠️ No objects detected or no results available")

def track_players_and_bags(video_path):
    results = model.track(video_path, persist=True)
    print(f"Tracking done. Results type: {type(results)}, Length: {len(results) if isinstance(results, list) else 'N/A'}")
    
    # Write detected objects to file
    write_detected_objects_to_file(results)
    
    return results
