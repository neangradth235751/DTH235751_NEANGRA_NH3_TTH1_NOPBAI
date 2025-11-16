from tkinter import *

def TaoManHinhStyleButton():
    root = Tk()
    root.title("frame 2") # Tiêu đề cửa sổ
    root.configure(bg="#ECECEC") # Màu nền xám nhạt

    # Danh sách các kiểu relief (style) khác nhau
    relief_styles = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']
    
    # Danh sách các giá trị borderwidth (độ dày viền)
    border_widths = [0, 1, 2, 3, 4]
    
    # --- Tạo các nút bấm theo lưới ---
    
    # Hàng 0: Tiêu đề các kiểu relief
    for c, style in enumerate(relief_styles):
        Label(root, text=style, bg="#ECECEC", font=('Arial', 10, 'bold')).grid(row=0, column=c+1, padx=5, pady=5)
    
    # Các hàng còn lại: borderwidth và các nút bấm
    for r, bw in enumerate(border_widths):
        # Label hiển thị borderwidth
        Label(root, text=f"borderwidth = {bw}", bg="#ECECEC").grid(row=r+1, column=0, padx=5, pady=5, sticky=W)
        
        # Tạo các nút bấm với borderwidth và relief tương ứng
        for c, style in enumerate(relief_styles):
            # Cấu hình nút
            btn = Button(root, 
                         text=style,
                         relief=style,           # Thiết lập kiểu relief
                         borderwidth=bw,         # Thiết lập độ dày viền
                         height=1, 
                         width=8)
            
            # Nếu là kiểu 'solid' và bw > 0, có thể làm nổi bật hơn
            if style == 'solid' and bw > 0:
                 btn.config(bg='black', fg='white')
            
            # Bố trí nút vào lưới
            btn.grid(row=r+1, column=c+1, padx=5, pady=5)

    root.mainloop()

# Chạy chương trình
TaoManHinhStyleButton()
