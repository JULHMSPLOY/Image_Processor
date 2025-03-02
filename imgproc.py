import os
import multiprocessing
from PIL import Image

def process_image(image_path, output_folder):
    try:
        with Image.open(image_path) as img:
            img_gray = img.convert('L')