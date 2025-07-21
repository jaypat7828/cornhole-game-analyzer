from ultralytics import YOLO
import os
import yaml

# Load custom labels from labels.yaml
def load_custom_labels():
    try:
        with open('labels.yaml', 'r') as f:
            data = yaml.safe_load(f)
            return data.get('track_labels', [])
    except FileNotFoundError:
        print("⚠️ labels.yaml not found, using all YOLO classes")
        return []

# Load custom labels
custom_labels = load_custom_labels()
print(f"Custom labels loaded: {custom_labels}")

model = YOLO("models/yolov8n.pt")

def filter_results_by_labels(results):
    """
    Filter YOLO results to only include objects from our custom labels
    """
    if not custom_labels:
        return results
    
    filtered_results = []
    for result in results:
        if hasattr(result, 'boxes') and result.boxes is not None:
            # Get indices of boxes that match our custom labels
            keep_indices = []
            if hasattr(result.boxes, 'cls') and result.boxes.cls is not None:
                for i, cls_id in enumerate(result.boxes.cls):
                    if cls_id < len(result.names):
                        object_name = result.names[int(cls_id)]
                        if object_name in custom_labels:
                            keep_indices.append(i)
            
            # Create a new result with only the filtered boxes
            if keep_indices:
                # Use the new() method to create a new Results object
                filtered_result = result.new()
                # Update the boxes with only the filtered ones
                filtered_result.boxes = result.boxes[keep_indices]
                filtered_results.append(filtered_result)
            else:
                # No matching objects in this frame, create empty result
                filtered_result = result.new()
                filtered_result.boxes = None
                filtered_results.append(filtered_result)
        else:
            filtered_results.append(result)
    
    return filtered_results

def write_detected_objects_to_file(results):
    """
    Extract unique detected objects from YOLO results and write them to detected_objects.txt
    Only include objects that match our custom labels
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
                                # Only include objects from our custom labels
                                if object_name in custom_labels:
                                    unique_objects.add(object_name)
    
    # Write unique objects to file
    if unique_objects:
        with open('detected_objects.txt', 'w') as f:
            for obj in sorted(unique_objects):
                f.write(f"{obj}\n")
        print(f"✅ Unique detected objects written to detected_objects.txt: {sorted(unique_objects)}")
    else:
        print("⚠️ No objects from custom labels detected")
        # Create empty file
        with open('detected_objects.txt', 'w') as f:
            pass

def track_players_and_bags(video_path):
    results = model.track(video_path, persist=True)
    print(f"Tracking done. Results type: {type(results)}, Length: {len(results) if isinstance(results, list) else 'N/A'}")
    
    # Filter results to only include objects from custom labels
    filtered_results = filter_results_by_labels(results)
    print(f"Filtered to only include objects: {custom_labels}")
    
    # Write detected objects to file
    write_detected_objects_to_file(filtered_results)
    
    return filtered_results
