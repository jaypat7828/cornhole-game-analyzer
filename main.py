from tracker import track_players_and_bags
from scorer import calculate_score_and_annotate
from utils import save_annotated_video

def process_video(input_path):
    frames, fps = track_players_and_bags(input_path)
    annotated_frames = calculate_score_and_annotate(frames)
    output_path = save_annotated_video(annotated_frames, fps)
    return output_path