from tkinter import *
from tkinter import messagebox

def chuyen_doi_action():
    """Xử lý khi nhấn nút Chuyển."""
    try:
        # Lấy giá trị độ F và chuyển sang float
        do_f = float(input_do_f.get())
        
        # Công thức chuyển đổi: C = (F - 32) * 5/9
        do_c = (do_f - 32) * 5 / 9
        
        # Hiển thị kết quả, làm tròn đến 2 chữ số thập phân
        output_do_c.set(f"{do_c:.2f}°C")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ cho độ F.")
        output_do_c.set("Lỗi nhập liệu")

# --- KHỞI TẠO VÀ BỐ TRÍ GIAO DIỆN ---

root = Tk()
root.title("Chuyển Đổi Độ F sang Độ C")
root.geometry("250x150")
root.resizable(False, False)

# Đặt màu nền chung (Giống hình minh họa)
BG_COLOR = "#FFFFD0" 
root.configure(bg=BG_COLOR) 

# Biến StringVar
input_do_f = StringVar()
input_do_f.set("350") # Giá trị mặc định
output_do_c = StringVar()
output_do_c.set("Độ C ở đây")

# --- Bố trí các thành phần (Grid) ---

# Hàng 1: Nhập độ F
Label(root, text="Nhập độ F", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=1, column=0, padx=5, pady=10, sticky="w")
Entry(root, width=15, textvariable=input_do_f, fg="red", justify='center', bd=2).grid(row=1, column=1, padx=5, pady=10)

# Hàng 2: Nút Chuyển
Button(root, text="Chuyển", command=chuyen_doi_action, bg="#4682B4", fg="white", font=('Tahoma', 10, 'bold'), width=10).grid(row=2, column=1, pady=5)

# Hàng 3: Độ C (Label tiêu đề)
Label(root, text="Độ C", bg=BG_COLOR, font=('Tahoma', 10)).grid(row=3, column=0, padx=5, pady=10, sticky="w")

# Hàng 3: Kết quả Độ C
Entry(root, width=15, textvariable=output_do_c, fg="blue", justify='center', bd=2, state='readonly').grid(row=3, column=1, padx=5, pady=10)

root.mainloop()
