from image_loader import load_image, convert_to_rgb
from frame_extractor import extract_frames
from preprocessing import resize_image, normalize_image, convert_color_space
from utils import save_image
import os
from PIL import Image

def preprocess_image(file_path, output_path, size=(256, 256), color_space='RGB'):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")
    
    image = load_image(file_path)
    
    if image is None:
        raise ValueError(f"Failed to load image from '{file_path}'")
    
    if file_path.lower().endswith(('.tif', '.tiff')):
        frames = extract_frames(file_path)
        preprocessed_frames = []
        for frame in frames:
            frame = resize_image(frame, size)
            frame = normalize_image(frame)
            frame = convert_color_space(frame, color_space)
            preprocessed_frames.append(frame)
        for idx, frame in enumerate(preprocessed_frames):
            save_image(frame, f"{output_path}_frame_{idx}.png")
    else:
        image = convert_to_rgb(image)
        image = resize_image(image, size)
        image = normalize_image(image)
        image = convert_color_space(image, color_space)
        save_image(image, f"{output_path}.png")

if __name__ == "__main__":
    preprocess_image('/Users/kavindev/Desktop/ISRO/ImageGPT/modules/image_preprocessing/sampleImages/sample2.tif', 
                     '/Users/kavindev/Desktop/ISRO/ImageGPT/modules/image_preprocessing/outputImages/output', 
                     size=(256, 256), 
                     color_space='RGB')
