# Image Processing with Multiprocessing
โปรแกรมสำหรับประมวลผลภาพแบบขนาน (parallel processing) หรือ การประมวลผลภาพหลายไฟล์พร้อมกัน โดยใช้ Multiprocessing และ Pillow (PIL) เพื่อช่วยให้การประมวลผลภาพมีประสิทธิภาพและรวดเร็วมากขึ้น ซึ่งแต่ละภาพจะถูกประมวลผลตามลำดับ ดังนี้

- เปิดไฟล์ภาพจากโฟลเดอร์ที่กำหนด
- แปลงภาพเป็นขาวดำ (Grayscale)
- ปรับขนาดภาพเป็น 128x128 pixels
- บันทึกไฟล์ภาพที่ถูกประมวลผลแล้วไปยังโฟลเดอร์ปลายทาง
  
# Programming Language
- Python สำหรับการประมวลผลภาพ การจัดการไฟล์ และการใช้งานการประมวลผลขนาน (parallel processing)
  

# Libraries
- os: จัดการไฟล์และโฟลเดอร์  เช่น การตรวจสอบการมีอยู่ของโฟลเดอร์ การสร้างโฟลเดอร์ใหม่ การจัดการกับเส้นทางของไฟล์ เป็นต้น
- Multiprocessing: โปรแกรมสามารถประมวลผลหลายๆงานพร้อมกันได้ โดยเฉพาะในการประมวลผลภาพจำนวนมาก
- Pillow (PIL): เปิด, แก้ไข, บันทึกรูปภาพ, รองรับ format ต่างๆ เช่น .jpg, .png, .jpeg และการประมวลผลภาพ เช่น การแปลงภาพเป็นขาวดำ (grayscale) การปรับขนาดภาพ (resize) เป็นต้น
- tqdm: แสดงแถบสถานะความคืบหน้าของโปรแกรมในขณะประมวลผล ช่วยให้ผู้ใช้งานเห็นสถานะของการประมวลผลแบบเรียลไทม์

# Features
- การประมวลผลภาพหลายๆ ไฟล์พร้อมกัน (parallel processing)
- แปลงภาพเป็นขาวดำ (Grayscale)
- ปรับขนาดภาพเป็น 128x128 พิกเซล
- แสดงแถบสถานะความคืบหน้าแบบเรียลไทม์

# Directory Structure

```sh
Image_Processor/
│
├── input_images/           # โฟลเดอร์ที่เก็บภาพที่ต้องการประมวลผล
│   ├── cat1.jpg
│   ├── cat2.jpg
│   ├── cat3.jpg
│   ├── cat4.jpg
│   ├── cat5.jpg
│   ├── dog1.png
│   ├── dog2.png
│   ├── dog3.png
│   ├── dog4.png
│   └── dog5.png
│
├── output_images/          # โฟลเดอร์ที่เก็บภาพที่ประมวลผลแล้ว
│   ├── processed_cat1.jpg  # ตัวอย่างผลลัพธ์หลังจากการประมวลผล
│   └── processed_dog3.png  
│
├── LICENSE.md              # ข้อกำหนดลิขสิทธิ์ของ Project
├── README.md               # คำอธิบาย Project
├── imgproc.py              # สคริปต์ Python ที่ใช้ในการประมวลผลภาพ                    
└── requirements.txt        # ไฟล์ที่ใช้ระบุไลบรารีที่ Project ต้องการ
```

# Setup
- Pillow สำหรับการประมวลผลภาพ
  
```sh
pip install pillow
```

- tqdm สำหรับแสดงแถบสถานะความคืบหน้า

```sh
pip install tqdm
```

# Usage
- เปิดไฟล์ภาพ, แปลงภาพเป็นขาวดำ (Grayscale), ปรับขนาดภาพเป็น 128x128 pixels และบันทึกภาพที่ประมวลผลแล้ว

```sh
# เปิดภาพและแปลงเป็นภาพขาวดำ (grayscale)
with Image.open(image_path) as img:
    img_gray = img.convert('L')
    # ปรับขนาดของภาพเป็น 128x128 พิกเซล            
    img_resized = img_gray.resize((128, 128))
```

```sh
    # บันทึกรูปภาพที่ประมวลผลแล้ว 
    img_resized.save(output_path)         
```

- ตรวจสอบการมีอยู่ของโฟลเดอร์ปลายทาง, ค้นหาไฟล์ภาพในโฟลเดอร์ input_folder, ประมวลผลภาพหลายไฟล์พร้อมกัน และแสดงแถบสถานะความคืบหน้า

```sh
# ตรวจสอบว่าโฟลเดอร์ที่ใช้เก็บภาพที่ประมวลผลแล้วมีอยู่หรือไม่ ถ้าไม่มีให้สร้างขึ้นมา
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# สร้างรายการไฟล์ภาพทั้งหมดในโฟลเดอร์ input_folder ที่มีนามสกุล .jpg, .png, หรือ .jpeg
image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith(('jpg', 'png', 'jpeg'))]
```

```sh
# ใช้ multiprocessing.Pool เพื่อประมวลผลไฟล์ภาพหลายๆ ไฟล์พร้อมกัน
# tqdm ใช้ในการแสดงแถบความคืบหน้า
with multiprocessing.Pool() as pool:
    list(tqdm(pool.starmap(process_image, [(image, output_folder) for image in image_files]), total=len(image_files)))
```

# Getting Started
- Clone the repository
  
```sh
git clone https://github.com/username/Image_Processor.git
```
- Install dependencies

```sh
pip install -r requirements.txt
```

- สามารถเพิ่มรูปภาพที่ต้องการประมวลผลได้ในโฟลเดอร์ input_images
  
```sh
Image_Processor/
│
├── input_images/           # โฟลเดอร์ที่เก็บภาพที่ต้องการประมวลผล
│   ├── cat1.jpg
│   ├── cat2.jpg
│   ├── cat3.jpg
│   ├── cat4.jpg
│   ├── cat5.jpg
│   ├── dog1.png
│   ├── dog2.png
│   ├── dog3.png
│   ├── dog4.png
│   ├── dog5.png
│   └── ...
```

- ระบุ path ของโฟลเดอร์ในตัวแปร input_folder และ output_folder
  
```sh
input_folder = "input_images"    # ระบุโฟลเดอร์ที่มีภาพที่ต้องการประมวลผล
output_folder = "output_images"  # ระบุโฟลเดอร์ที่เก็บภาพที่ประมวลผลแล้ว
```

- Run the Program
```sh
python imgproc.py
```

- Output After Running the Program
```sh
├── output_images/          # โฟลเดอร์ที่เก็บภาพที่ประมวลผลแล้ว
│   ├── processed_cat1.jpg  # ตัวอย่างผลลัพธ์หลังจากการประมวลผล
│   ├── processed_dog3.png
│   └── ...
```
# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
