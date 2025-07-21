# Cornhole Game Analyzer

A computer vision system for analyzing cornhole games using YOLO object detection and tracking. The system detects specific objects in cornhole gameplay videos and provides annotation capabilities.

## 🎯 Project Goal

The primary goal is to detect and analyze cornhole game elements (players, sandbags, board) to provide automated scoring and game statistics. Currently, the system focuses on object detection and video annotation for specific game elements.

## 📊 Current Status

### ✅ Completed Features
- **Object Detection**: YOLOv8n model integration for detecting objects in cornhole videos
- **Custom Label Filtering**: System filters detections to only include objects from `labels.yaml`
- **Video Annotation**: Automatic annotation of detected objects on video frames
- **Object Tracking**: YOLO tracking with persistence across frames
- **Output Generation**: Creates annotated videos and logs detected objects

### 🎯 Current Detection Targets
Based on `labels.yaml`, the system currently detects:
- **Frisbee** (as proxy for sandbags)
- **Sports Ball** (additional game elements)
- **Kite** (testing object)

### 📁 Output Files
- `detected_objects.txt` - List of unique objects detected in the video
- `outputs/output.mp4` - Annotated video with bounding boxes and labels

## 🏗️ Project Structure

```
cornhole-game-analyzer/
├── 📁 models/                    # YOLO model weights
│   └── yolov8n.pt               # Pre-trained YOLOv8n model
├── 📁 outputs/                   # Generated output files
│   └── output.mp4               # Annotated video output
├── 📁 samples/                   # Input video samples
├── 📁 venv/                      # Python virtual environment
├── 📁 .venv/                     # Alternative virtual environment
├── 📄 app.py                     # Streamlit web interface
├── 📄 main.py                    # Core video processing pipeline
├── 📄 tracker.py                 # YOLO object detection and tracking
├── 📄 scorer.py                  # Scoring logic (placeholder)
├── 📄 utils.py                   # Utility functions for video handling
├── 📄 labels.yaml                # Custom object labels configuration
├── 📄 requirements.txt           # Python dependencies
├── 📄 download_model.py          # Model download script
├── 📄 Makefile                   # Build and run automation
├── 📄 README.md                  # This file
└── 📄 LICENSE                    # Project license
```

## 🔧 Important Files Explained

### Core Processing Files

#### `main.py` - Video Processing Pipeline
- **Purpose**: Orchestrates the entire video analysis workflow
- **Key Functions**:
  - `process_video()`: Main entry point for video processing
  - Handles FPS detection and video output generation
  - Coordinates between tracking and scoring modules

#### `tracker.py` - Object Detection & Tracking
- **Purpose**: Handles YOLO-based object detection and tracking
- **Key Functions**:
  - `track_players_and_bags()`: Main tracking function
  - `filter_results_by_labels()`: Filters detections to custom labels
  - `write_detected_objects_to_file()`: Logs unique detected objects
  - `load_custom_labels()`: Loads labels from `labels.yaml`

#### `scorer.py` - Game Scoring Logic
- **Purpose**: Analyzes bag positions to determine scoring
- **Status**: Currently a placeholder for future scoring implementation
- **Future**: Will analyze bag trajectories and landing positions

#### `utils.py` - Video Utilities
- **Purpose**: Handles video file operations
- **Key Functions**:
  - `save_annotated_video()`: Saves processed videos with annotations

### Configuration Files

#### `labels.yaml` - Object Labels Configuration
```yaml
track_labels:
  - frisbee      # Proxy for sandbags
  - sports ball  # Additional game elements
  - kite         # Testing object
```

#### `requirements.txt` - Dependencies
- **Core**: `ultralytics`, `opencv-python`, `torch`
- **Web Interface**: `streamlit`
- **Data Processing**: `numpy`, `pandas`, `moviepy`
- **Configuration**: `PyYAML`

### Interface Files

#### `app.py` - Streamlit Web Interface
- **Purpose**: Provides web-based interface for video upload and processing
- **Features**: File upload, processing status, result display

#### `Makefile` - Automation Scripts
- **Purpose**: Provides convenient commands for common tasks
- **Commands**: Model download, environment setup, app running

## 🚀 How It Works

### 1. Video Input
- Upload video through Streamlit interface or direct file processing
- System supports common video formats (MP4, AVI, etc.)

### 2. Object Detection
- YOLOv8n model processes each video frame
- Detects all objects present in the frame
- Filters results to only include objects from `labels.yaml`

### 3. Object Tracking
- YOLO tracking with persistence across frames
- Maintains object IDs throughout the video
- Handles object occlusion and re-appearance

### 4. Video Annotation
- Draws bounding boxes around detected objects
- Labels objects with their class names
- Shows tracking IDs for persistent objects

### 5. Output Generation
- Creates annotated video in `outputs/` directory
- Generates `detected_objects.txt` with unique object list
- Provides processing statistics and logs

## 🔄 Next Steps

### Immediate Priority: Sandbag Detection
1. **Model Retraining**: Train YOLO model specifically on cornhole sandbags
2. **Dataset Collection**: Gather cornhole game videos with sandbag annotations
3. **Label Updates**: Update `labels.yaml` to include proper sandbag labels
4. **Model Integration**: Replace current model with custom-trained sandbag detector

### Future Enhancements
1. **Scoring Algorithm**: Implement automatic scoring based on bag positions
2. **Player Tracking**: Separate player detection from bag detection
3. **Game Statistics**: Generate player performance metrics
4. **Real-time Processing**: Enable live video analysis
5. **Multi-camera Support**: Handle multiple camera angles

## 🛠️ Setup and Usage

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (optional, for faster processing)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd cornhole-game-analyzer

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
make install

# Download YOLO model
make download-model

# make help
make help
```

### Usage
```bash
# Run Streamlit web interface
make run
```

## 📝 Technical Details

### Model Architecture
- **Base Model**: YOLOv8n (nano variant for speed)
- **Input**: Video frames (RGB)
- **Output**: Bounding boxes, class labels, confidence scores
- **Tracking**: YOLO's built-in tracking with persistence

### Performance Considerations
- YOLOv8n provides good balance of speed and accuracy
- GPU acceleration recommended for real-time processing
- Video processing time depends on video length and resolution

### Customization
- Modify `labels.yaml` to change detection targets
- Adjust confidence thresholds in tracker.py
- Customize annotation styles in utils.py

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
