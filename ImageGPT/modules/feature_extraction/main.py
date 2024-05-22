from ImageGPT.modules.image_preprocessing.main import preprocess_image
from ImageGPT.modules.feature_extraction.extractor import extract_features
# from ImageGPT.modules.image_preprocessing.image_loader import load_image, convert_to_rgb

def process_image(image):
    print("Processing image...")
    features = extract_features(image)
    print("Features extracted:", features)
    return features

if __name__ == "__main__":
    # Preprocess the image
    preprocessed_images = preprocess_image(
        '/Users/kavindev/Desktop/ISRO/ImageGPT/modules/image_preprocessing/sampleImages/sample3.jpeg',
        '/Users/kavindev/Desktop/ISRO/ImageGPT/modules/image_preprocessing/output',
        size=(256, 256),
        color_space='RGB'
    )

    # Ensure preprocessing returned valid images
    if preprocessed_images is None:
        raise ValueError("Preprocessing failed, no images returned")
    
    print(f"Preprocessed images type: {type(preprocessed_images)}")

    if isinstance(preprocessed_images, list):
        for idx, image in enumerate(preprocessed_images):
            print(f"Processing frame {idx}...")
            if image is None:
                print(f"Frame {idx} is None")
                continue
            features = process_image(image)
            print(f"Features from frame {idx}: {features}")
    else:
        if preprocessed_images is None:
            raise ValueError("Preprocessed image is None")
        features = process_image(preprocessed_images)
        print("Features extracted:", features)
