import cv2
import numpy as np
from PIL import Image
from preprocessing import preprocess_image

def not_operation(image_path):
    """
    Perform NOT operation on a preprocessed grayscale image.
    
    :param image_path: Path to the input image.
    :return: Image after applying NOT operation.
    """
    # Read the image as grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Ensure the image is loaded properly
    if image is None:
        raise ValueError(f"Error: Unable to load image from {image_path}")

    # Apply NOT operation
    not_image = cv2.bitwise_not(image)
    
    return not_image
