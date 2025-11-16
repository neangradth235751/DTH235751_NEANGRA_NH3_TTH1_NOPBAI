from tkinter import *
from tkinter import messagebox

# Hàm xử lý khi nhấn nút OK (Giả định logic)
def ok_action():
    old_pass = old_pass_var.get()
    new_pass = new_pass_var.get()
    confirm_pass = confirm_pass_var.get()
    
    # Logic kiểm tra đơn giản
    if not old_pass or not new_pass or not confirm_pass:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")
    elif new_pass != confirm_pass:
        messagebox.showerror("Lỗi", "Mật khẩu mới và Xác nhận mật khẩu không khớp.")
    else:
        # Giả định logic thành công
        messagebox.showinfo("Thành công", "Mật khẩu đã được thay đổi!")
        root.destroy()

# Hàm xử lý khi nhấn nút Cancel
def cancel_action():
    root.destroy()

# --- KHỞI TẠO VÀ BỐ TRÍ GIAO DIỆN ---

root = Tk()
root.title("Enter New Password")
# Đặt kích thước cố định và màu nền xám nhạt mô phỏng giao diện cũ
root.geometry("300x150")
root.resizable(False, False)
root.configure(bg="#ECECEC") 

# Biến StringVar cho các ô nhập liệu
old_pass_var = StringVar()
new_pass_var = StringVar()
confirm_pass_var = StringVar()

# --- Tiêu đề (Sử dụng Label với màu nền khác) ---
Label(root, text="Enter New Password", bg="#99BADD", fg="black", font=("Arial", 10, 'bold'), anchor="w") \
    .grid(row=0, columnspan=2, sticky="ew") # sticky="ew" giúp Label lấp đầy chiều rộng

# --- Các Label và Entry cho Mật khẩu ---
# Hàng 1: Old Password
Label(root, text="Old Password:", bg="#ECECEC", font=("Arial", 9)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=20, show="*", textvariable=old_pass_var).grid(row=1, column=1, padx=5, pady=5)

# Hàng 2: New Password
Label(root, text="New Password:", bg="#ECECEC", font=("Arial", 9)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=20, show="*", textvariable=new_pass_var).grid(row=2, column=1, padx=5, pady=5)

# Hàng 3: Enter New Password Again
Label(root, text="Enter New Password Again:", bg="#ECECEC", font=("Arial", 9)).grid(row=3, column=0, padx=5, pady=5, sticky="w")
Entry(root, width=20, show="*", textvariable=confirm_pass_var).grid(row=3, column=1, padx=5, pady=5)

# --- Khung chứa các Nút bấm ---
frameButton = Frame(root, bg="#ECECEC")

Button(frameButton, text="OK", command=ok_action, width=8).pack(side=LEFT, padx=10)
Button(frameButton, text="Cancel", command=cancel_action, width=8).pack(side=LEFT, padx=10)

# Bố trí Khung chứa nút ở hàng cuối cùng
frameButton.grid(row=4, columnspan=2, pady=10)

root.mainloop()
