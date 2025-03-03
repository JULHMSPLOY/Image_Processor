import os # ใช้สำหรับจัดการไฟล์และโฟลเดอร์ 
import multiprocessing # ใช้สำหรับประมวลผลแบบขนาน (parallel processing) 
from PIL import Image # สำหรับการเปิดและประมวลผลรูปภาพ
from tqdm import tqdm # สำหรับแสดงแถบสถานะความคืบหน้า

# ฟังก์ชันในการประมวลผลรูปภาพ
def process_image(image_path, output_folder):
    try:
        # แสดงช้อความเริ่มต้นการเปิดรูปภาพ
        print(f"Opening image: {image_path}")

        # เปิดภาพและแปลงเป็นภาพขาวดำ (grayscale)
        with Image.open(image_path) as img:
            img_gray = img.convert('L')

            # ปรับขนาดของภาพเป็น 128x128 พิกเซล
            img_resized = img_gray.resize((128, 128))

            # สร้าง path สำหรับบันทึกรูปภาพที่ถูกประมวลผล
            filename = os.path.basename(image_path)
            output_path = os.path.join(output_folder, f"processed_{filename}")
            
            # บันทึกรูปภาพที่ประมวลผลแล้ว
            print(f"Saving image to: {output_path}")
            img_resized.save(output_path)
            print(f"Processed and saved: {output_path}")
    except Exception as e:
        # ถ้ามีข้อผิดพลาดในการประมวลผลให้แสดงข้อความของข้อผิดพลาด
        print(f"Error processing {image_path}: {e}")

# ฟังก์ชันหลักในการเริ่มต้นการประมวลผล
def main(input_folder, output_folder):
    # ตรวจสอบว่าโฟลเดอร์ที่ใช้เก็บภาพที่ประมวลผลแล้วมีอยู่หรือไม่ ถ้าไม่มีให้สร้างขึ้นมา
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # สร้างรายการไฟล์ภาพทั้งหมดในโฟลเดอร์ input_folder ที่มีนามสกุล .jpg, .png, หรือ .jpeg
    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('jpg', 'png', 'jpeg'))]

    print(f"Found {len(image_files)} images to process.")

    # ถ้าไม่มีไฟล์ภาพในโฟลเดอร์ให้แสดงข้อความแจ้ง
    if len(image_files) == 0:
        print("No images found.")
        return

    # ใช้ multiprocessing.Pool เพื่อประมวลผลไฟล์ภาพหลายๆ ไฟล์พร้อมกัน
    # tqdm ใช้ในการแสดงแถบความคืบหน้า
    with multiprocessing.Pool() as pool:
        list(tqdm(pool.starmap(process_image, [(image, output_folder) for image in image_files]), total = len (image_files)))

# ฟังก์ชันเริ่มต้นเมื่อโปรแกรมรัน
if __name__ == "__main__":
    input_folder = "input_images"    # ระบุโฟลเดอร์ที่มีภาพที่ต้องการประมวลผล
    output_folder = "output_images"  # ระบุโฟลเดอร์ที่เก็บภาพที่ประมวลผลแล้ว

    # เรียกใช้ฟังก์ชัน main เพื่อเริ่มต้นการประมวลผล
    main(input_folder, output_folder) 