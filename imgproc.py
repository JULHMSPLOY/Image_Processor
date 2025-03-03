import os
import multiprocessing
from PIL import Image
from tqdm import tqdm

def process_image(image_path, output_folder):
    try:
        print(f"Opening image: {image_path}")
        with Image.open(image_path) as img:
            img_gray = img.convert('L')
            img_resized = img_gray.resize((128, 128))

            filename = os.path.basename(image_path)
            output_path = os.path.join(output_folder, f"processed_{filename}")
            
            print(f"Saving image to: {output_path}")
            img_resized.save(output_path)
            print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('jpg', 'png', 'jpeg'))]

    print(f"Found {len(image_files)} images to process.")

    if len(image_files) == 0:
        print("No images found.")
        return

    with multiprocessing.Pool() as pool:
        list(tqdm(pool.starmap(process_image, [(image, output_folder) for image in image_files]), total = len (image_files)))

if __name__ == "__main__":
    input_folder = "input_images"  
    output_folder = "output_images"

    main(input_folder, output_folder) 