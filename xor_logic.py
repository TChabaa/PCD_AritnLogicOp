import cv2
import numpy as np

def xor_operation(image_path1, image_path2):

    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    if image1 is None or image2 is None:
        raise ValueError("One or both images could not be loaded.")

    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    or_image = cv2.bitwise_xor(image1, image2)

    return or_image