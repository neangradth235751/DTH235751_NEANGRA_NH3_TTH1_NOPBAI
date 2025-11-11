import os

def lay_ten_file_va_duoi(duong_dan: str) -> str:
    """
    Hàm lấy ra tên file hoàn chỉnh (ví dụ: muabui.mp3) từ đường dẫn.
    """
    # os.path.basename() sẽ trả về phần cuối cùng của đường dẫn (tên file).
    ten_file = os.path.basename(duong_dan)
    return ten_file

def lay_ten_bai_hat(duong_dan: str) -> str:
    """
    Hàm lấy ra chỉ tên bài hát, loại bỏ phần mở rộng (ví dụ: muabui).
    """
    # 1. Lấy tên file hoàn chỉnh (muabui.mp3)
    ten_file_hoan_chinh = os.path.basename(duong_dan)
    
    # 2. Tách tên file và phần mở rộng
    # os.path.splitext() trả về một tuple: (tên_file_gốc, phần_mở_rộng)
    ten_goc, duoi = os.path.splitext(ten_file_hoan_chinh)
    
    return ten_goc

# --- Ví dụ kiểm tra ---
duong_dan_mau = r"d:\music\muabui.mp3"  # Ký tự 'r' để xử lý chuỗi raw, tránh lỗi '\m'

print(f"Đường dẫn đầu vào: {duong_dan_mau}")
print("-" * 30)

# Yêu cầu 1: Lấy ra muabui.mp3
ten_file = lay_ten_file_va_duoi(duong_dan_mau)
print(f"1. Tên file và đuôi (muabui.mp3): {ten_file}")

# Yêu cầu 2: Lấy ra muabui
ten_bai_hat = lay_ten_bai_hat(duong_dan_mau)
print(f"2. Tên bài hát (muabui): {ten_bai_hat}")

# Ví dụ kiểm tra với đường dẫn phức tạp hơn hoặc không có thư mục
duong_dan_khac = r"/home/user/songs/tay_bac_goi_em.FLAC"
print("\n--- Ví dụ khác ---")
print(f"Đường dẫn đầu vào: {duong_dan_khac}")
print(f"1. Tên file và đuôi: {lay_ten_file_va_duoi(duong_dan_khac)}")
print(f"2. Tên bài hát: {lay_ten_bai_hat(duong_dan_khac)}")
