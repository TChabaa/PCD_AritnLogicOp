import cv2
import numpy as np

def and_not_operation(image_path1, image_path2):
    """
    Perform AND-NOT operation on two preprocessed grayscale images.
    
    :param image_path1: Path to the first input image (A).
    :param image_path2: Path to the second input image (B).
    :return: Image after applying AND-NOT operation.
    """
    # Read both images as grayscale
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    
    # Ensure images are loaded properly
    if image1 is None:
        raise ValueError(f"Error: Unable to load image from {image_path1}")
    if image2 is None:
        raise ValueError(f"Error: Unable to load image from {image_path2}")
    
    # Resize images to the same dimensions if needed
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    
    # Apply NOT operation on the second image
    not_image2 = cv2.bitwise_not(image2)
    
    # Apply AND operation between image1 and NOT image2
    and_not_result = cv2.bitwise_and(image1, not_image2)
    
    return and_not_result
