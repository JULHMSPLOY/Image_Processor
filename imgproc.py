import os
import multiprocessing
from PIL import Image

def process_image(image_path, output_folder):
    try:
        with Image.open(image_path) as img:
            img_gray = img.convert('L')
            img_resized = img_gray.resize((128, 128))

            filename = os.path.basename(image_path)