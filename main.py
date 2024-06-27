from moviepy.editor import VideoFileClip
import os

def get_vid_dynamic_bitrate(video_path, resolution_target) -> str:
    vid_clip = VideoFileClip(video_path)
    current_bitrate = vid_clip.reader.bitrate
    current_resolution = vid_clip.size
    scaling_factor = ( (resolution_target[0] * resolution_target[1]) / (current_resolution[0] * current_resolution[1]) )
    
    return f"{int(current_bitrate * scaling_factor)}k"


def video_compressor( input_path, output_path, target_resolution=(1280, 720) ) -> None:
    # Get video
    vid_clip = VideoFileClip(input_path)
    
    # Resizing the video
    resized_clip = vid_clip.resize(height=target_resolution[1])
    
    # Getting dynamic bitrate based on the current video properties
    dynamic_bitrate = get_vid_dynamic_bitrate(input_path, target_resolution)
    
    # Saving the resized video
    resized_clip.write_videofile(output_path, bitrate=dynamic_bitrate, codec="libx264")
    
    return None


if __name__ == "__main__":
    video_path = "transformer.mp4"
    output_video_path = "compressed.mp4"
    
    # Compress Video
    video_compressor(video_path, output_video_path)
    print(f"{video_path} was successfuly compressed and saved as {output_video_path}")