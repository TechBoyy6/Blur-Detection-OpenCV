import cv2
import numpy as np

def readImage(path):
    image = cv2.imread(path)
    return image


def show_images(image):
    scale_percent = 10
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    cv2.imshow("a", cv2.resize(image, dim, interpolation=cv2.INTER_AREA))
    cv2.waitKey(0)
