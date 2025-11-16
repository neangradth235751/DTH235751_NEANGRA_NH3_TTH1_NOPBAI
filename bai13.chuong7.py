import xml.etree.ElementTree as ET
import os

# Tên file
FILE_NHOM = 'nhomthietbi.xml'
FILE_TB = 'thietbi.xml'

# --- 1. HÀM XỬ LÝ FILE XML ---

def doc_xml(file_path):
    """Đọc và trả về gốc (root) của cây XML."""
    if not os.path.exists(file_path):
        print(f"Lỗi: Không tìm thấy file {file_path}. Đã tạo dữ liệu mẫu.")
        if file_path == FILE_NHOM:
            tao_du_lieu_nhom_mau()
        elif file_path == FILE_TB:
            tao_du_lieu_thiet_bi_mau()
            
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except Exception as e:
        print(f"Lỗi đọc file {file_path}: {e}")
        return None

# --- 2. HÀM TẠO DỮ LIỆU MẪU ---
# Dùng để khởi tạo file nếu chưa có, giúp chương trình chạy lần đầu

def tao_du_lieu_nhom_mau():
    """Tạo file nhomthietbi.xml mẫu."""
    root = ET.Element('nhoms')
    
    nhom1 = ET.SubElement(root, 'nhom')
    ET.SubElement(nhom1, 'ma').text = 'n1'
    ET.SubElement(nhom1, 'ten').text = 'Nhóm 1'

    nhom2 = ET.SubElement(root, 'nhom')
    ET.SubElement(nhom2, 'ma').text = 'n2'
    ET.SubElement(nhom2, 'ten').text = 'Nhóm 2'
    
    tree = ET.ElementTree(root)
    tree.write(FILE_NHOM, encoding='UTF-8', xml_declaration=True)

def tao_du_lieu_thiet_bi_mau():
    """Tạo file ThietBi.xml mẫu."""
    root = ET.Element('thietbis')
    
    tb1 = ET.SubElement(root, 'thietbi', manhom='n1')
    ET.SubElement(tb1, 'ma').text = 'tb1'
    ET.SubElement(tb1, 'ten').text = 'Thiết bị 1'

    tb2 = ET.SubElement(root, 'thietbi', manhom='n1')
    ET.SubElement(tb2, 'ma').text = 'tb2'
    ET.SubElement(tb2, 'ten').text = 'Thiết bị 2'
    
    tb3 = ET.SubElement(root, 'thietbi', manhom='n2')
    ET.SubElement(tb3, 'ma').text = 'tb3'
    ET.SubElement(tb3, 'ten').text = 'Thiết bị 3'

    tree = ET.ElementTree(root)
    tree.write(FILE_TB, encoding='UTF-8', xml_declaration=True)

# --- 3. CHỨC NĂNG CHÍNH ---

def lay_ten_nhom(ma_nhom, nhom_root):
    """Lấy tên nhóm từ mã nhóm."""
    for nhom in nhom_root.findall('nhom'):
        if nhom.find('ma').text == ma_nhom:
            return nhom.find('ten').text
    return "Không rõ"

def hien_thi_nhom_thiet_bi(nhom_root):
    """Hiển thị danh sách Nhóm thiết bị."""
    print("\n--- DANH SÁCH NHÓM THIẾT BỊ ---")
    for nhom in nhom_root.findall('nhom'):
        ma = nhom.find('ma').text
        ten = nhom.find('ten').text
        print(f"Mã: {ma}\tTên Nhóm: {ten}")

def hien_thi_toan_bo_thiet_bi(tb_root, nhom_root):
    """Hiển thị toàn bộ Thiết bị với tên nhóm tương ứng."""
    print("\n--- DANH SÁCH TOÀN BỘ THIẾT BỊ ---")
    print("Mã TB\tTên Thiết Bị\tMã Nhóm\tTên Nhóm")
    print("-" * 50)
    for tb in tb_root.findall('thietbi'):
        ma = tb.find('ma').text
        ten = tb.find('ten').text
        ma_nhom = tb.get('manhom') # Lấy thuộc tính manhom
        ten_nhom = lay_ten_nhom(ma_nhom, nhom_root)
        print(f"{ma}\t{ten}\t{ma_nhom}\t{ten_nhom}")

def loc_thiet_bi_theo_nhom(tb_root, nhom_root):
    """Lọc Danh sách Thiết bị theo Nhóm thiết bị."""
    hien_thi_nhom_thiet_bi(nhom_root)
    ma_loc = input("\nNhập Mã Nhóm cần lọc: ").strip()
    
    ten_nhom = lay_ten_nhom(ma_loc, nhom_root)
    if ten_nhom == "Không rõ":
        print(f"Lỗi: Không tìm thấy nhóm có mã {ma_loc}.")
        return

    print(f"\n--- THIẾT BỊ THUỘC NHÓM {ten_nhom} ({ma_loc}) ---")
    tim_thay = False
    for tb in tb_root.findall('thietbi'):
        if tb.get('manhom') == ma_loc:
            ma = tb.find('ma').text
            ten = tb.find('ten').text
            print(f"Mã TB: {ma}\tTên: {ten}")
            tim_thay = True
            
    if not tim_thay:
        print("Không có thiết bị nào trong nhóm này.")

def xuat_nhom_co_so_luong_thiet_bi_nhieu_nhat(tb_root, nhom_root):
    """Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất."""
    dem_nhom = {} # Dictionary đếm số lượng TB theo mã nhóm
    
    # 1. Đếm số lượng thiết bị trong mỗi nhóm
    for tb in tb_root.findall('thietbi'):
        ma_nhom = tb.get('manhom')
        dem_nhom[ma_nhom] = dem_nhom.get(ma_nhom, 0) + 1
        
    if not dem_nhom:
        print("Không có thiết bị nào được ghi nhận.")
        return

    # 2. Tìm số lượng lớn nhất
    max_count = max(dem_nhom.values())
    
    # 3. Lọc ra các nhóm có số lượng bằng số lớn nhất
    nhom_nhieu_nhat = {ma: count for ma, count in dem_nhom.items() if count == max_count}

    print("\n--- NHÓM CÓ SỐ LƯỢNG THIẾT BỊ NHIỀU NHẤT ---")
    for ma_nhom, count in nhom_nhieu_nhat.items():
        ten_nhom = lay_ten_nhom(ma_nhom, nhom_root)
        print(f"Nhóm: {ten_nhom} (Mã: {ma_nhom}) có {count} thiết bị.")

# --- CHƯƠNG TRÌNH CHÍNH (MENU) ---

def ChayQLThietBi():
    # Đảm bảo file tồn tại trước khi chạy
    nhom_root = doc_xml(FILE_NHOM)
    tb_root = doc_xml(FILE_TB)

    if nhom_root is None or tb_root is None:
        print("Không thể khởi tạo chương trình do lỗi file XML.")
        return

    print("\n========== QUẢN LÝ THIẾT BỊ (XML) ==========")
    while True:
        print("\n1. Xem DS Nhóm | 2. Xem Toàn bộ TB | 3. Lọc TB theo Nhóm | 4. Nhóm có TB nhiều nhất | 0. Thoát")
        chon = input("Chọn chức năng: ").strip()
        
        if chon == '1':
            hien_thi_nhom_thiet_bi(nhom_root)
        elif chon == '2':
            hien_thi_toan_bo_thiet_bi(tb_root, nhom_root)
        elif chon == '3':
            loc_thiet_bi_theo_nhom(tb_root, nhom_root)
        elif chon == '4':
            xuat_nhom_co_so_luong_thiet_bi_nhieu_nhat(tb_root, nhom_root)
        elif chon == '0':
            print("Kết thúc chương trình Quản Lý Thiết Bị.")
            break
        else:
            print("Chọn không hợp lệ.")

if __name__ == "__main__":
    # Khởi tạo file mẫu lần đầu
    if not os.path.exists(FILE_NHOM):
        tao_du_lieu_nhom_mau()
    if not os.path.exists(FILE_TB):
        tao_du_lieu_thiet_bi_mau()
        
    ChayQLThietBi()
