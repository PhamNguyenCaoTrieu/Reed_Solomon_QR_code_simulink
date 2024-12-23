# Cài đặt thư viện quét và sửa lỗi QR
import os

os.system('pip install qrcode[pil]')
os.system('pip install pillow')
os.system('pip install pyzbar')
from PIL import Image
from pyzbar.pyzbar import decode


# 1. Quét QR code từ file ảnh
def read_qr_code(filename):
    try:
        img = Image.open(filename)
        result = decode(img)

        if result:
            for obj in result:
                print("Dữ liệu giải mã:", obj.data.decode("utf-8"))
        else:
            print("Không thể giải mã QR code.")
    except Exception as e:
        print(f"Lỗi khi đọc QR code: {e}")


# 2. Làm hỏng QR code
# Tại đây chỉnh phần QR lỗi
def damage_qr_code_with_color(filename="hinh_goc.jpg",
                              damaged_filename="hinh_loi.png"):
    try:
        # Mở ảnh QR code
        img = Image.open(filename).convert(
            "RGB")  # Chuyển sang chế độ RGB để hỗ trợ màu
        pixels = img.load()
        # Lấy kích thước ảnh
        width, height = img.size
        box_size = 100
        start_x = width // 2 - box_size // 2
        start_y = height // 2 - box_size // 2
        end_x = start_x + box_size
        end_y = start_y + box_size
        # Làm hỏng vùng chính giữa bằng cách đổi pixel thành màu trắng
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                pixels[x, y] = (255, 255, 255)  # Lỗi màu trắng
# Lưu ảnh sau khi làm hỏng
        img.save(damaged_filename)
        print(f"QR code bị lỗi với màu được lưu tại: {damaged_filename}")
    except Exception as e:
        print(f"Lỗi khi làm hỏng QR code: {e}")


# 3. Chương trình chính
if __name__ == "__main__":
    original_file = "hinh_goc.jpg"  # Ảnh gốc
    damaged_file = "hinh_loi.png"  # Ảnh lỗi
    # Quét QR code gốc
    print("\nĐọc QR code gốc:")
    read_qr_code(original_file)
    # Làm hỏng QR code
    print("\nĐang làm hỏng QR code...")
    damage_qr_code_with_color(original_file, damaged_file)
    # Quét QR code bị lỗi
    print("\nĐọc QR code bị lỗi:")
    read_qr_code(damaged_file)
