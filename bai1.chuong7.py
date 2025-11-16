# Tên file: XuLyFile.py

def LuuFile(path, data):
    """
    Ghi dữ liệu sản phẩm vào file. Dữ liệu mới được thêm vào cuối file ('a').
    """
    # Mở file với chế độ 'a' (append) và mã hóa UTF-8
    file = open(path, 'a', encoding='utf-8')
    
    # Ghi chuỗi dữ liệu (ví dụ: "masp;tensp;dongia")
    file.write(data)
    
    # Ghi ký tự xuống dòng
    file.write("\n")
    
    # Đóng file
    file.close()

def DocFile(path):
    """
    Đọc dữ liệu sản phẩm từ file và trả về một list các list (danh sách sản phẩm).
    """
    arrProduct = []
    
    try:
        # Mở file với chế độ 'r' (read)
        file = open(path, 'r', encoding='utf-8')
        
        for line in file:
            # Loại bỏ khoảng trắng/xuống dòng ở hai đầu
            data = line.strip()
            
            # Tách chuỗi thành các thuộc tính (mã SP, tên SP, đơn giá)
            arr = data.split(';')
            
            # Kiểm tra nếu dòng không rỗng thì thêm vào danh sách
            if len(arr) == 3:
                arrProduct.append(arr)
        
        # Đóng file
        file.close()
        
    except FileNotFoundError:
        print(f"Lỗi: File '{path}' không tồn tại. Danh sách rỗng được trả về.")

    return arrProduct
