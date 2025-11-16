from tkinter import *

# Hàm xử lý nút "Tiếp" (Reset)
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

# Hàm xử lý nút "Giải"
def giaiAction():
    try:
        # Lấy giá trị và chuyển sang float
        a = float(stringHSA.get())
        b = float(stringHSB.get())
    except ValueError:
        stringKQ.set("Lỗi: Hệ số không hợp lệ!")
        return
        
    # Logic giải phương trình ax + b = 0
    if a == 0:
        if b == 0:
            stringKQ.set("Vô số nghiệm")
        else: # a = 0 và b != 0
            stringKQ.set("Vô nghiệm")
    else: # a != 0
        x = -b / a
        # Format kết quả chỉ lấy 2 chữ số thập phân nếu cần
        stringKQ.set(f"x = {x:.2f}")

# --- Khởi tạo GUI ---

root = Tk()
stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

root.title("PTB1 - facebook.com/duythanhcse")
root.minsize(height=130, width=250)
root.resizable(height=True, width=True)

# Tiêu đề
# Chú ý: Đã sửa lỗi xuống dòng trong chuỗi "Phương Trình Bậc 1"
Label(root, text="Phương Trình Bậc 1", fg="red", font=("Tahoma", 16), justify=CENTER).grid(row=0, columnspan=2, pady=5)

# Hàng 1: Hệ số a
Label(root, text="Hệ số a:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1, padx=5)

# Hàng 2: Hệ số b
Label(root, text="Hệ số b:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1, padx=5)

# Khung chứa các nút bấm
frameButton = Frame(root)
Button(frameButton, text="Giải", command=giaiAction).pack(side=LEFT, padx=5, pady=10)
Button(frameButton, text="Tiếp", command=tiepAction).pack(side=LEFT, padx=5, pady=10)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT, padx=5, pady=10)
frameButton.grid(row=3, columnspan=2)

# Hàng 4: Kết quả
Label(root, text="Kết quả:").grid(row=4, column=0, padx=5, pady=5, sticky=W)
Entry(root, width=30, textvariable=stringKQ, state='readonly').grid(row=4, column=1, padx=5) # Đặt state='readonly' cho kết quả

root.mainloop()
