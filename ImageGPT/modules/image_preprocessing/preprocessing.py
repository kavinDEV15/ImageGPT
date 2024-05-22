from PIL import Image
import numpy as np

def resize_image(image, size):
    if isinstance(image, Image.Image):
        return image.resize(size)
    else:
        raise ValueError("resize_image: input is not a PIL Image")


def normalize_image(image):
    array = np.asarray(image).astype(np.float32) / 255.0
    return Image.fromarray((array * 255).astype(np.uint8))

def convert_color_space(image, color_space='RGB'):
    return image.convert(color_space)
