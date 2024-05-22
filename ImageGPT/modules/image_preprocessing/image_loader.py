from PIL import Image
import rasterio
from osgeo import gdal

def load_image(file_path):
    if file_path.lower().endswith(('jpg', 'jpeg', 'png')):
        return Image.open(file_path)
    elif file_path.lower().endswith(('tif', 'tiff')):
        with rasterio.open(file_path) as src:
            return src.read(1)  # Read the first band as an array
    else:
        return None

def convert_to_rgb(image):
    if isinstance(image, Image.Image):
        return image.convert('RGB')
    elif isinstance(image, gdal.Dataset):
        array = image.ReadAsArray()
        if array.shape[0] == 6:  # Assuming 3-band image
            return array.transpose(1, 2, 0)
        else:
            raise ValueError("Unsupported number of bands for conversion.")
    else:
        raise TypeError("Unsupported image type")
