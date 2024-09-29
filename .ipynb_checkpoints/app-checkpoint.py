# app.py

import cv2
from PIL import Image, ImageFilter
import os

def apply_grayscale(image_path, save_path):
    """
    Applies grayscale filter to the image.
    """
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(save_path, gray_img)
    print(f"Grayscale image saved at: {save_path}")

def apply_blur(image_path, save_path):
    """
    Applies blur filter to the image.
    """
    img = Image.open(image_path)
    blurred_img = img.filter(ImageFilter.BLUR)
    blurred_img.save(save_path)
    print(f"Blurred image saved at: {save_path}")

def show_image(image_path):
    """
    Displays the image.
    """
    img = Image.open(image_path)
    img.show()

if __name__ == "__main__":
    # Paths
    image_path = "images/sample_image.jpg"
    grayscale_path = "filters/grayscale_image.jpg"
    blur_path = "filters/blurred_image.jpg"
    
    # Apply filters
    apply_grayscale(image_path, grayscale_path)
    apply_blur(image_path, blur_path)

    # Display images
    show_image(grayscale_path)
    show_image(blur_path)
 
