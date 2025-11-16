# --- 1. Định nghĩa Hàm Xử lý File ---

def LuuFile(path, data):
    """Ghi dữ liệu (data) vào cuối file (path)."""
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()

def DocFile(path):
    """Đọc dữ liệu từ file, trả về list các list chuỗi số."""
    arrSo = []
    
    try:
        file = open(path, 'r', encoding='utf-8')
        
        for line in file:
            data = line.strip()
            # Tách chuỗi dựa trên dấu phẩy
            arr = data.split(',')
            
            # Chỉ thêm vào nếu dòng có dữ liệu
            if any(arr):
                arrSo.append(arr)
        
        file.close()
        
    except FileNotFoundError:
        print(f"Lỗi: File '{path}' không tồn tại.")
        
    return arrSo

# --- 2. Tạo Dữ liệu Mẫu (Ghi đè hoặc xóa file cũ trước khi chạy lần đầu) ---

# Ghi dữ liệu vào file (Chế độ 'a' sẽ nối thêm. 
# Nếu muốn bắt đầu lại, hãy mở file bằng 'w' trước khi chạy LuuFile lần đầu)

# Ghi các dòng dữ liệu vào csdl_so.txt
LuuFile("csdl_so.txt","-5,4,7,9,3,20")
LuuFile("csdl_so.txt","5,-4,37,-19,24,-21")
LuuFile("csdl_so.txt","15,9,0,-38,-3,15")
LuuFile("csdl_so.txt","5,-4,77,-9,3,-7")
LuuFile("csdl_so.txt","55,44,27")
LuuFile("csdl_so.txt","-50,26")

# --- 3. Xử lý và Xuất ---

# Đọc lại dữ liệu vừa tạo
arrSo = DocFile("csdl_so.txt")
print("Dữ liệu đọc được từ file (dạng list các list chuỗi):")
print(arrSo)

def XuatSoAmTrenMoiDong(arrSo):
    """Duyệt qua list và in các số âm trên từng dòng."""
    for row in arrSo:
        found_negative_on_row = False
        for element in row:
            try:
                # Chuyển chuỗi thành số nguyên
                number = int(element)
                
                if number < 0:
                    print(number, end='\t')
                    found_negative_on_row = True
            except ValueError:
                # Bỏ qua nếu không phải số
                pass
        
        # Xuống dòng nếu có in số âm trên dòng đó
        if found_negative_on_row:
            print() 

print("\nCác số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)
