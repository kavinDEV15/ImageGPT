import cv2

def initialize_orb():
    return cv2.ORB_create()

def convert_to_gray(image):
    if image is None:
        print("Image is None in convert_to_gray")
        return None
    if len(image.shape) == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

def extract_orb_features(image, orb):
    gray_image = convert_to_gray(image)
    if gray_image is None:
        print("Gray image is None in extract_orb_features")
        return None
    keypoints, descriptors = orb.detectAndCompute(gray_image, None)
    return descriptors

def extract_features(image):
    orb = initialize_orb()
    descriptors_orb = extract_orb_features(image, orb)
    return {
        'orb': descriptors_orb,
    }
