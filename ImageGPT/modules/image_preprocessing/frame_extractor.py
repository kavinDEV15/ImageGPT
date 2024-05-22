from PIL import Image
import rasterio

def extract_frames(file_path):
    frames = []
    with rasterio.open(file_path) as src:
        for i in range(src.count):
            frame = src.read(i + 1)  # Read each band as an array
            frames.append(Image.fromarray(frame))
    return frames

