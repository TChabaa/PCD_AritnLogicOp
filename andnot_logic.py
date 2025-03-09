import cv2
import numpy as np

def and_not_operation(image_path1, image_path2):
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
    
    # Apply AND operation on the both image
    and_result = cv2.bitwise_and(image1, image2)
    
    # Perform NOT operation on the AND result
    and_not_result = cv2.bitwise_not(and_result)
    
    return and_not_result
