import json
import os

FILE_LOPHOC = 'lophoc.json'
FILE_SINHVIEN = 'sinhvien.json'

# --- HÀM XỬ LÝ FILE (Đọc/Ghi JSON) ---

def DocJson(file_path):
    """Đọc dữ liệu từ file JSON và trả về List."""
    data = []
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return data
        
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Lỗi: File {file_path} không đúng định dạng JSON.")
            return []
    return data

def LuuJson(file_path, data):
    """Ghi List dữ liệu vào file JSON."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- CHỨC NĂNG QUẢN LÝ SINH VIÊN ---

def LayTenLop(ma_lop):
    """Lấy tên lớp từ mã lớp."""
    lop_list = DocJson(FILE_LOPHOC)
    for lop in lop_list:
        if lop['Ma'] == ma_lop:
            return lop['Ten']
    return "Không rõ"

def HienThiDSSV(dssv):
    """Hiển thị danh sách sinh viên."""
    if not dssv:
        print("Danh sách rỗng.")
        return
    print("\n----------------------------------------------------")
    print("Mã\tTên Sinh Viên\t\tNăm Sinh\tLớp")
    print("----------------------------------------------------")
    for sv in dssv:
        ten_lop = LayTenLop(sv['MaLop'])
        print(f"{sv['Ma']}\t{sv['Ten']}\t{sv['NamSinh']}\t\t{ten_lop}")
    print("----------------------------------------------------")

def ThemMoiSinhVien():
    """Thêm mới một sinh viên."""
    sv_list = DocJson(FILE_SINHVIEN)
    
    ma_sv = input("Nhập Mã SV: ").strip()
    if any(sv['Ma'] == ma_sv for sv in sv_list):
        print("Lỗi: Mã sinh viên đã tồn tại.")
        return

    ten_sv = input("Nhập Tên SV: ").strip()
    try:
        nam_sinh = int(input("Nhập Năm Sinh: "))
        ma_lop = input("Nhập Mã Lớp (MaLop): ").strip()
    except ValueError:
        print("Lỗi: Năm sinh không hợp lệ.")
        return

    sv_moi = {
        'Ma': ma_sv,
        'Ten': ten_sv,
        'NamSinh': nam_sinh,
        'MaLop': ma_lop
    }
    
    sv_list.append(sv_moi)
    LuuJson(FILE_SINHVIEN, sv_list)
    print("Thêm sinh viên thành công.")

def XoaSinhVien():
    """Xóa một sinh viên theo mã."""
    sv_list = DocJson(FILE_SINHVIEN)
    ma_xoa = input("Nhập Mã SV cần xóa: ").strip()
    
    sv_moi = [sv for sv in sv_list if sv['Ma'] != ma_xoa]
    
    if len(sv_moi) < len(sv_list):
        LuuJson(FILE_SINHVIEN, sv_moi)
        print(f"Sinh viên {ma_xoa} đã được xóa.")
    else:
        print(f"Lỗi: Không tìm thấy sinh viên có mã {ma_xoa}.")

def SapXepSinhVien():
    """Sắp xếp sinh viên theo Năm Sinh."""
    sv_list = DocJson(FILE_SINHVIEN)
    if not sv_list:
        print("Danh sách rỗng.")
        return
        
    # Sắp xếp theo cột 'NamSinh'
    sv_list.sort(key=lambda sv: sv['NamSinh'], reverse=False) # Sắp xếp tăng dần theo năm sinh
    HienThiDSSV(sv_list)

# --- CHẠY CHƯƠNG TRÌNH MẪU CÂU 10 ---

def ChayQLSinhVien():
    # Khởi tạo dữ liệu lớp học mẫu nếu chưa có
    if not os.path.exists(FILE_LOPHOC):
        LuuJson(FILE_LOPHOC, [{'Ma': 'CNTT01', 'Ten': 'Lập trình Python'}, {'Ma': 'KTOAN02', 'Ten': 'Kế Toán Cơ Bản'}])

    print("\n\n=============== QUẢN LÝ SINH VIÊN (JSON) ===============")
    
    while True:
        print("\n1. Xem DS SV | 2. Thêm SV | 3. Xóa SV | 4. Sắp xếp (Năm Sinh) | 0. Thoát")
        chon = input("Chọn chức năng: ")
        
        if chon == '1':
            HienThiDSSV(DocJson(FILE_SINHVIEN))
        elif chon == '2':
            ThemMoiSinhVien()
        elif chon == '3':
            XoaSinhVien()
        elif chon == '4':
            SapXepSinhVien()
        elif chon == '0':
            print("Kết thúc chương trình Quản Lý Sinh Viên.")
            break
        else:
            print("Chọn không hợp lệ.")

# Chạy chương trình chính (bỏ dấu # để chạy)
# ChayQLSanPham()
# ChayQLSinhVien()
