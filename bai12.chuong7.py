import csv
import random
import os

FILE_NAME = 'nhanvien_data.csv'

# --- HÀM 1: LƯU TẬP TIN CSV NGẪU NHIÊN ---

def LuuFileCSVNgauNhien(path):
    """
    Tạo và lưu 10 dòng dữ liệu vào file CSV.
    Mỗi dòng gồm 10 số nguyên ngẫu nhiên cách nhau bởi dấu chấm phẩy (;).
    """
    try:
        # Sử dụng 'w' để ghi đè, tạo file mới mỗi lần chạy
        with open(path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            
            so_dong = 10
            so_so_moi_dong = 10
            
            for _ in range(so_dong):
                # Tạo một list chứa 10 số nguyên ngẫu nhiên (ví dụ: từ 1 đến 100)
                # Dùng list comprehension để tạo nhanh hơn
                row = [random.randrange(1, 100) for _ in range(so_so_moi_dong)]
                
                # Ghi dòng dữ liệu vào file
                writer.writerow(row)
                
        print(f"✅ Đã khởi tạo và lưu file '{path}' thành công với 10 dòng dữ liệu ngẫu nhiên.")
        
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

# --- HÀM 2: ĐỌC VÀ TÍNH TỔNG GIÁ TRỊ TRÊN MỖI DÒNG ---

def DocFileCSVVaTinhTong(path):
    """
    Đọc file CSV, tính tổng giá trị của các phần tử trên mỗi dòng và xuất ra màn hình.
    """
    if not os.path.exists(path):
        print(f"❌ Lỗi: File '{path}' không tồn tại. Vui lòng chạy hàm LuuFileCSVNgauNhien trước.")
        return

    print(f"\n--- Đọc File '{path}' và Tính Tổng Giá Trị ---")
    
    try:
        # Mở file để đọc ('r')
        with open(path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            
            for i, row in enumerate(reader):
                dong_hien_tai = i + 1
                tong_gia_tri = 0
                
                # Tính tổng các giá trị trong dòng
                for element in row:
                    try:
                        # Chuyển đổi phần tử (chuỗi) sang số nguyên để tính tổng
                        tong_gia_tri += int(element)
                    except ValueError:
                        # Bỏ qua nếu có phần tử không phải là số
                        pass
                
                # Xuất kết quả
                print(f"Dòng {dong_hien_tai}: {', '.join(row[:5])}..., Tổng = {tong_gia_tri}")
                
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

# --- CHƯƠNG TRÌNH CHÍNH ---

def ChayChuongTrinhCSV():
    # 1. Khởi tạo và Lưu file
    LuuFileCSVNgauNhien(FILE_NAME)
    
    # 2. Đọc file và Tính Tổng
    DocFileCSVVaTinhTong(FILE_NAME)

ChayChuongTrinhCSV()
