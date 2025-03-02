import os
import multiprocessing
from PIL import Image

def process_image(image_path, output_folder):
    try:
        with Image.open(image_path) as img:
            img_gray = img.convert('L')
            img_resized = img_gray.resize((128, 128))

            filename = os.path.basename(image_path)
            output_path = os.path.join(output_folder, f"processed_{filename}")

            img_resized.save(output_path)
            print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")