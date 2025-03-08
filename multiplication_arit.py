import cv2
import numpy as np

def multiplication_operation(image_path1, image_path2):

    image1 = cv2.imread(image_path1, cv2.IMREAD_COLOR)
    image2 = cv2.imread(image_path2, cv2.IMREAD_COLOR)
    
    if image1 is None or image2 is None:
        raise ValueError("One or both images could not be loaded.")
    
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    
    result = cv2.multiply(image1, image2)
    
    return result
