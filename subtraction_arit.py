import cv2
import numpy as np

def subtraction_operation(image_path1, image_path2):
    """
    Perform pixel-wise subtraction of two images.
    
    :param image_path1: Path to the first image.
    :param image_path2: Path to the second image.
    :return: Processed image after subtraction.
    """
    image1 = cv2.imread(image_path1, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image_path2, cv2.IMREAD_COLOR)

    if image1 is None or image2 is None:
        raise ValueError("One or both images could not be loaded.")
    
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Perform pixel-wise subtraction (clipped at 0 to prevent underflow)
    result = cv2.subtract(image1, image2)
    
    return result
