from tkinter import *

# Biến toàn cục để lưu chuỗi nhập liệu
expression = ""

# --- HÀM XỬ LÝ NÚT BẤM ---

def press(num):
    """Xử lý khi người dùng bấm các nút số và phép toán."""
    global expression
    # Nối số/phép toán vào chuỗi hiện tại
    expression = expression + str(num)
    # Cập nhật hiển thị
    equation.set(expression)

def equalpress():
    """Xử lý khi người dùng bấm nút '='."""
    global expression
    try:
        # Dùng hàm eval() để tính toán biểu thức
        total = str(eval(expression))
        equation.set(total)
        # Thiết lập lại biểu thức sau khi tính
        expression = total
    except:
        # Xử lý lỗi (ví dụ: chia cho 0 hoặc cú pháp sai)
        equation.set(" Lỗi ")
        expression = ""

def clear():
    """Xử lý khi người dùng bấm nút 'Clr' (Xóa toàn bộ)."""
    global expression
    expression = ""
    equation.set("")

# --- KHỞI TẠO VÀ BỐ TRÍ GIAO DIỆN ---

root = Tk()
root.title("Máy Tính Bỏ Túi")
root.geometry("240x270") # Thiết lập kích thước cửa sổ
root.resizable(False, False) # Không cho phép thay đổi kích thước
root.configure(bg="#F0F0F0")

# Biến StringVar để hiển thị trên màn hình
equation = StringVar()

# Tạo khung hiển thị kết quả
expression_field = Entry(root, textvariable=equation, font=('Arial', 16), bd=5, relief=SUNKEN, justify='right')
expression_field.grid(row=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5)

# --- TẠO CÁC NÚT BẤM ---

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '-', '0', '.',
    '+', '*', '/', '=',
    'Clr'
]

r = 1 # Bắt đầu từ hàng 1
c = 0 # Bắt đầu từ cột 0

for button_text in buttons:
    # Nếu là nút 'Clr', chiếm 4 cột cuối cùng
    if button_text == 'Clr':
        btn = Button(root, text=button_text, fg='black', bg='#D3D3D3',
                     command=clear, height=2, width=20, font=('Arial', 10, 'bold'))
        btn.grid(row=r+1, columnspan=4, padx=5, pady=5)
        break # Kết thúc vòng lặp sau nút 'Clr'

    # Thiết lập lệnh command cho các nút
    if button_text == '=':
        command_func = equalpress
        bg_color = '#FFA07A' # Màu cam nhạt cho nút '='
    elif button_text in ('+', '-', '*', '/'):
        command_func = lambda x=button_text: press(x)
        bg_color = '#ADD8E6' # Màu xanh nhạt cho phép toán
    else:
        command_func = lambda x=button_text: press(x)
        bg_color = '#FFFFFF' # Màu trắng cho số

    btn = Button(root, text=button_text, fg='black', bg=bg_color,
                 command=command_func, height=2, width=5, font=('Arial', 10, 'bold'))
    
    # Bố trí nút
    btn.grid(row=r, column=c, padx=5, pady=5)

    # Chuyển cột và hàng
    c += 1
    if c > 2:
        c = 0
        r += 1

root.mainloop()
