import cv2
import numpy as np

# ye number different images try karke mila hai
blur_factor = 1000


def readImage(path):
    """@param path : The path of the images
@brief Reads the image and return it in gray scale"""
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return image


def show_images(image):
    """@brief This function rescales the images and displays it on the screen"""
    scale_percent = 10
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    cv2.imshow("a", cv2.resize(image, dim, interpolation=cv2.INTER_AREA))
    cv2.waitKey(0)

def method_laplacian(img):
    """@brief Here the Laplacian method is applied and variance of the image is returned
@param img takes gray scale image"""
    lap_factor = cv2.Laplacian(img, cv2.CV_64F).var()
    print(lap_factor)
    return lap_factor

def main():
    path = "sample\SAVE_20220107_100133.jpg"
    img = readImage(path)
    factor = method_laplacian(img)
    if(factor<blur_factor):
        print("Image to blur")
    else:
        print("This Image can work")

main()