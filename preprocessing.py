import numpy as np
import cv2

def preprocess_image(image_path):
    """
    :param image_path: Path to the input image.
    :return: Preprocessed image as a NumPy array.
    """
    # Read image using OpenCV
    image = preprocess_image(image_path)
    if image is None:
        return None
    not_image = cv2.bitwise_not(image)
    return not_image

    return image