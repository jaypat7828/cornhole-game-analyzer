# cornhole-game-analyzer
Analyze a cornhole game and generate player stats.

# Directory Structure:
# cornhole_tracker/
# ├── app.py                  # Streamlit app
# ├── main.py                 # Core logic
# ├── scorer.py               # Scoring logic
# ├── tracker.py              # Player/bag tracking logic
# ├── utils.py                # Helper functions
# ├── requirements.txt        # Python dependencies
# └── Makefile                # Build/Run automation

models/ – for the YOLOv8 model weights.

samples/ – place your input .mp4 videos here.

outputs/ – processed videos will be saved here.


Download YOLOv8 (nano is fastest for testing):


# requirements.txt
# opencv-python
# streamlit
# ultralytics  # YOLOv8
# numpy
# pandas
# moviepy
# torch

# Makefile

# app.py (Streamlit Frontend)

# main.py

# tracker.py
# Placeholder: use YOLO or similar to track players and bags

# scorer.py
# Placeholder: use bag position across frames to determine if it landed in hole or on board

# utils.py
