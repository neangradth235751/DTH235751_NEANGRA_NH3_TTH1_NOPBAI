from tkinter import *
from tkinter import messagebox

# Bảng phân loại BMI theo tiêu chuẩn quốc tế đơn giản (từ hình ảnh)
# Ghi chú: Chúng ta sẽ đơn giản hóa phần "Nguy cơ phát triển bệnh" để khớp với logic chính
# Tình trạng: [Phạm vi BMI thấp nhất, Tình trạng]
# Nguy cơ: [Phạm vi BMI thấp nhất, Nguy cơ]

def phan_loai_bmi(bmi):
    """Phân loại tình trạng cân nặng và nguy cơ bệnh dựa trên chỉ số BMI."""
    if bmi < 18.5:
        return "Gầy", "Thấp"
    elif 18.5 <= bmi <= 24.9:
        return "Bình thường", "Trung bình"
    elif 25.0 <= bmi <= 29.9:
        return "Mập", "Cao"
    else: # BMI >= 30.0
        return "Béo phì", "Rất Cao"

def tinh_bmi_action():
    """Xử lý khi nhấn nút 'Tính BMI'."""
    try:
        # Lấy giá trị Chiều cao và Cân nặng
        # Chú ý: Chiều cao phải là mét, Cân nặng phải là kilogram.
        # Dữ liệu mẫu (1.8m, 172kg) gợi ý cân nặng đang nhập là gam hoặc không chính xác, 
        # nhưng ta vẫn dùng giá trị nhập vào.
        # Giả định Chiều cao (H) là mét và Cân nặng (W) là kilogram.
        
        chieu_cao = float(input_chieu_cao.get())
        can_nang = float(input_can_nang.get())

        if chieu_cao <= 0 or can_nang <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và Cân nặng phải lớn hơn 0.")
            return

        # Tính toán BMI
        bmi = can_nang / (chieu_cao ** 2)
        
        # Phân loại
        tinh_trang, nguy_co = phan_loai_bmi(bmi)
        
        # Cập nhật kết quả lên giao diện
        output_bmi.set(f"{bmi:.2f}")
        output_tinh_trang.set(tinh_trang)
        output_nguy_co.set(nguy_co)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho Chiều cao và Cân nặng.")
        output_bmi.set("Lỗi")
        output_tinh_trang.set("")
        output_nguy_co.set("")

# --- KHỞI TẠO VÀ BỐ TRÍ GIAO DIỆN ---

root = Tk()
root.title("Phần Mềm Tính BMI")
root.geometry("300x300")
root.resizable(False, False)

# Đặt màu nền chung (Giống hình minh họa)
BG_COLOR = "#FFFFD0" 
root.configure(bg=BG_COLOR) 

# Biến StringVar
input_chieu_cao = StringVar()
input_chieu_cao.set("1.8")
input_can_nang = StringVar()
input_can_nang.set("72") # Chỉnh lại giá trị mẫu từ 172 (sai) thành 72 (hợp lý hơn cho 1.8m)
output_bmi = StringVar()
output_tinh_trang = StringVar()
output_nguy_co = StringVar()

# --- Bố trí các thành phần (Grid) ---

# Hàng 1: Nhập chiều cao
Label(root, text="Nhập chiều cao:", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=15, textvariable=input_chieu_cao, justify='center').grid(row=1, column=1, padx=5, pady=5)

# Hàng 2: Nhập cân nặng
Label(root, text="Nhập cân nặng:", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=15, textvariable=input_can_nang, justify='center').grid(row=2, column=1, padx=5, pady=5)

# Hàng 3: Nút Tính BMI
Button(root, text="Tính BMI", command=tinh_bmi_action, bg="#4682B4", fg="white", font=('Tahoma', 10, 'bold'), width=10).grid(row=3, columnspan=2, pady=10)

# Hàng 4: BMI của bạn
Label(root, text="BMI của bạn:", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=4, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=15, textvariable=output_bmi, justify='center', state='readonly').grid(row=4, column=1, padx=5, pady=5)

# Hàng 5: Tình trạng của bạn
Label(root, text="Tình trạng của bạn:", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=5, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=15, textvariable=output_tinh_trang, justify='center', state='readonly', fg="red").grid(row=5, column=1, padx=5, pady=5)

# Hàng 6: Nguy cơ phát triển bệnh
Label(root, text="Nguy cơ phát triển bệnh:", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=6, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=15, textvariable=output_nguy_co, justify='center', state='readonly', fg="orange").grid(row=6, column=1, padx=5, pady=5)

# Hàng 7: Nút Thoát
Button(root, text="Thoát", command=root.quit, bg="#D3D3D3", width=8).grid(row=7, columnspan=2, pady=10)

root.mainloop()
