import os
import csv
from operator import itemgetter

FILE_DANHMUC = 'danhmuc.txt'
FILE_SANPHAM = 'sanpham.txt'

# --- HÀM XỬ LÝ FILE (Đọc/Ghi) ---

def DocDuLieu(file_path):
    """Đọc dữ liệu từ file CSV/TXT và trả về List các List."""
    data = []
    if not os.path.exists(file_path):
        return data
        
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                data.append(row)
    return data

def LuuDuLieu(file_path, data):
    """Ghi List dữ liệu vào file CSV/TXT."""
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# --- CHỨC NĂNG QUẢN LÝ SẢN PHẨM ---

def LayTenDM(ma_dm):
    """Lấy tên danh mục từ mã DM."""
    dm_list = DocDuLieu(FILE_DANHMUC)
    for dm in dm_list:
        if dm[0] == ma_dm:
            return dm[1]
    return "Không rõ"

def HienThiDSSP(dssp):
    """Hiển thị danh sách sản phẩm ra màn hình."""
    if not dssp:
        print("Danh sách rỗng.")
        return
    print("\n----------------------------------------------------")
    print("Mã\tTên SP\t\tĐơn Giá\t\tDanh Mục")
    print("----------------------------------------------------")
    for sp in dssp:
        ma_sp, ten_sp, don_gia, ma_dm = sp
        ten_dm = LayTenDM(ma_dm)
        print(f"{ma_sp}\t{ten_sp}\t{don_gia}\t{ten_dm}")
    print("----------------------------------------------------")

def ThemMoiSanPham():
    """Thêm mới một sản phẩm."""
    sp_list = DocDuLieu(FILE_SANPHAM)
    
    ma_sp = input("Nhập Mã SP: ").strip()
    # Kiểm tra trùng lặp
    if any(sp[0] == ma_sp for sp in sp_list):
        print("Lỗi: Mã sản phẩm đã tồn tại.")
        return

    ten_sp = input("Nhập Tên SP: ").strip()
    try:
        don_gia = float(input("Nhập Đơn Giá: "))
        ma_dm = input("Nhập Mã Danh Mục (MaDM): ").strip()
    except ValueError:
        print("Lỗi: Đơn giá không hợp lệ.")
        return

    sp_list.append([ma_sp, ten_sp, str(don_gia), ma_dm])
    LuuDuLieu(FILE_SANPHAM, sp_list)
    print("Thêm sản phẩm thành công.")

def XoaSanPham():
    """Xóa một sản phẩm theo mã."""
    sp_list = DocDuLieu(FILE_SANPHAM)
    ma_xoa = input("Nhập Mã SP cần xóa: ").strip()
    
    sp_moi = [sp for sp in sp_list if sp[0] != ma_xoa]
    
    if len(sp_moi) < len(sp_list):
        LuuDuLieu(FILE_SANPHAM, sp_moi)
        print(f"Sản phẩm {ma_xoa} đã được xóa.")
    else:
        print(f"Lỗi: Không tìm thấy sản phẩm có mã {ma_xoa}.")

def SapXepSanPham():
    """Sắp xếp sản phẩm theo Đơn Giá."""
    sp_list = DocDuLieu(FILE_SANPHAM)
    if not sp_list:
        print("Danh sách rỗng.")
        return
        
    # Chuyển đơn giá từ chuỗi sang float để sắp xếp (itemgetter(2) là cột Đơn Giá)
    try:
        sp_list.sort(key=lambda x: float(x[2]), reverse=True) # Sắp xếp giảm dần
        HienThiDSSP(sp_list)
    except ValueError:
        print("Lỗi: Dữ liệu đơn giá không hợp lệ để sắp xếp.")

# --- CHẠY CHƯƠNG TRÌNH MẪU CÂU 9 ---

def ChayQLSanPham():
    # Khởi tạo dữ liệu danh mục mẫu nếu chưa có
    if not os.path.exists(FILE_DANHMUC):
        LuuDuLieu(FILE_DANHMUC, [['DM01', 'Điện Tử'], ['DM02', 'Thực Phẩm']])

    print("\n\n=============== QUẢN LÝ SẢN PHẨM (TXT) ===============")
    
    while True:
        print("\n1. Xem DS SP | 2. Thêm SP | 3. Xóa SP | 4. Sắp xếp (Giá) | 0. Thoát")
        chon = input("Chọn chức năng: ")
        
        if chon == '1':
            HienThiDSSP(DocDuLieu(FILE_SANPHAM))
        elif chon == '2':
            ThemMoiSanPham()
        elif chon == '3':
            XoaSanPham()
        elif chon == '4':
            SapXepSanPham()
        elif chon == '0':
            print("Kết thúc chương trình Quản Lý Sản Phẩm.")
            break
        else:
            print("Chọn không hợp lệ.")

# ChayQLSanPham()
