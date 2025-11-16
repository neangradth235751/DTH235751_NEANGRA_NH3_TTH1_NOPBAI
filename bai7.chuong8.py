from tkinter import *
from tkinter import messagebox

# Danh sách các Thiên Can (Can) và Địa Chi (Chi)
THIEN_CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
DIA_CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def tinh_can_chi(nam_duong_lich):
    """Tính Can và Chi của năm âm lịch tương ứng."""
    # Quy tắc tính Thiên Can: (Năm - 3) % 10
    # Canh ứng với 0 (như 1980), nên lấy (Năm - 3) % 10.
    # Tuy nhiên, quy tắc phổ biến hơn là lấy số cuối của năm trừ đi 3 hoặc chia lấy dư 10.
    # Ta dùng quy tắc: Can = Năm % 10 (Lấy số cuối của năm)
    # 0 (Canh) = 1980 -> (1980 % 10) = 0. THIÊN_CAN[0] = Canh
    # 1 (Tân) = 1981 -> (1981 % 10) = 1. THIÊN_CAN[1] = Tân
    # Nhóm 1: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý
    
    # Can: (Năm - 4) % 10
    # Vị trí: 0=Giáp, 1=Ất, ..., 9=Quý
    # 1984 (Giáp Tý): (1984 - 4) % 10 = 0 -> Giáp
    can_index = (nam_duong_lich - 4) % 10
    
    # Chi: (Năm - 4) % 12
    # Vị trí: 0=Tý, 1=Sửu, ..., 11=Hợi
    # 1984 (Giáp Tý): (1984 - 4) % 12 = 0 -> Tý
    chi_index = (nam_duong_lich - 4) % 12
    
    # Chú ý: Cấu trúc mảng THIEN_CAN và DIA_CHI cần được điều chỉnh 
    # để khớp với công thức (Năm - X) % Y
    # Cấu trúc đã chọn: THIEN_CAN[0] phải là Giáp (vì (1984-4)%10=0)
    # Cấu trúc cần: ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    
    # Dùng cấu trúc chuẩn:
    CAN_STANDARD = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    CHI_STANDARD = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    can = CAN_STANDARD[can_index]
    chi = CHI_STANDARD[chi_index]
    
    return f"{can} {chi}"

def chuyen_doi_action():
    """Xử lý khi nhấn nút Chuyển."""
    try:
        nam = int(input_nam.get())
        if nam < 0:
            messagebox.showerror("Lỗi", "Năm phải là số dương.")
            return

        can_chi = tinh_can_chi(nam)
        output_am_nam.set(can_chi)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên hợp lệ cho năm.")

# --- KHỞI TẠO VÀ BỐ TRÍ GIAO DIỆN ---

root = Tk()
root.title("Dương Lịch -> Âm Lịch (Can Chi)")
root.geometry("250x150")
root.resizable(False, False)

# Đặt màu nền chung (Giống hình minh họa)
root.configure(bg="#FFFFD0") 

# Biến StringVar
input_nam = StringVar()
input_nam.set("1982") # Giá trị mặc định
output_am_nam = StringVar()
output_am_nam.set("Nhâm Tuất") # Giá trị mặc định

# --- Bố trí các thành phần (Grid) ---

# Hàng 1: Nhập năm dương
Label(root, text="Nhập năm dương:", bg="#FFFFD0", font=('Tahoma', 10)).grid(row=1, column=0, padx=5, pady=10, sticky="w")
Entry(root, width=15, textvariable=input_nam, fg="red", justify='center', bd=2).grid(row=1, column=1, padx=5, pady=10)

# Hàng 2: Nút Chuyển
Button(root, text="Chuyển", command=chuyen_doi_action, bg="#4682B4", fg="white", font=('Tahoma', 10, 'bold'), width=10).grid(row=2, columnspan=2, pady=5)

# Hàng 3: Năm âm
Label(root, text="Năm âm:", bg="#FFFFD0", font=('Tahoma', 10)).grid(row=3, column=0, padx=5, pady=10, sticky="w")
Entry(root, width=15, textvariable=output_am_nam, fg="blue", justify='center', bd=2, state='readonly').grid(row=3, column=1, padx=5, pady=10)

root.mainloop()
