# tests/test_app.py

import os
from app import apply_grayscale, apply_blur

def test_apply_grayscale():
    image_path = "images/sample_image.jpg"
    save_path = "filters/test_grayscale.jpg"
    apply_grayscale(image_path, save_path)
    assert os.path.exists(save_path), "Grayscale image not saved properly."

def test_apply_blur():
    image_path = "images/sample_image.jpg"
    save_path = "filters/test_blur.jpg"
    apply_blur(image_path, save_path)
    assert os.path.exists(save_path), "Blurred image not saved properly."

if __name__ == "__main__":
    test_apply_grayscale()
    test_apply_blur()
    print("All tests passed!")
 
