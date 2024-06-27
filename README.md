### Description for GitHub Repository

---

# Video Compressor in Python

This repository contains a Python script to compress video files using `moviepy` and `Pillow` libraries. The script resizes video frames to a specified resolution and adjusts the bitrate dynamically based on the input video's properties to achieve efficient compression while maintaining quality.

## Features

- **Video Resizing**: Resizes video frames to a target resolution using high-quality downsampling with the `Pillow` library.
- **Dynamic Bitrate Adjustment**: Calculates and applies a dynamic bitrate based on the input video’s original bitrate and resolution.
- **Simple and Efficient**: Easy to use script that handles video compression efficiently, suitable for videos of various sizes.

## Requirements

- Python 3.x
- `moviepy` library
- `Pillow` library

## Installation

Install the required libraries using pip:

```sh
pip install moviepy pillow numpy
```

## Usage

1. Place your input video file in the same directory as the script or provide the full path to the video file.
2. Update the `input_video_path` and `output_video_path` variables in the script with your input and desired output file paths.
3. Run the script:

```sh
python compress_video.py
```

### Example Script

```python
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
```

## Notes

- Ensure you have enough memory and processing power to handle large video files.
- Adjust the `target_resolution` and `dynamic_bitrate` as needed to achieve the desired compression quality and file size.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this description further to match your repository structure and additional details you might want to include.
