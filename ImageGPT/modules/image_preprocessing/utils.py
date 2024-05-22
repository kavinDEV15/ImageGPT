import numpy as np
from PIL import Image

def save_image(image, path):
    if isinstance(image, np.ndarray):
        Image.fromarray(image).save(path)
    elif isinstance(image, Image.Image):
        image.save(path)
    else:
        raise TypeError("Unsupported image type")
