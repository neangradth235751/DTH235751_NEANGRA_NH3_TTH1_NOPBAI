def ToiUuChuoi(s):
    # Bước 1: Xóa khoảng trắng dư thừa ở hai đầu chuỗi
    s2 = s.strip()
    
    # Bước 2: Tách chuỗi thành các từ dựa trên khoảng trắng.
    # Khi dùng split(' ') trên chuỗi có nhiều khoảng trắng, 
    # nó sẽ tạo ra các phần tử rỗng ('') giữa các khoảng trắng.
    arr = s2.split(' ')
    
    s2 = ""
    
    # Bước 3: Lặp qua các phần tử, chỉ giữ lại các từ không rỗng
    for x in arr:
        word = x
        
        # Kiểm tra xem từ sau khi loại bỏ khoảng trắng dư thừa (nếu có) có rỗng không
        if len(word.strip()) != 0:
            # Nối từ lại và thêm một khoảng trắng sau mỗi từ
            s2 = s2 + word + " "
            
    # Bước 4: Xóa khoảng trắng cuối cùng và trả về chuỗi tối ưu
    return s2.strip()

# --- Đoạn mã kiểm tra ---
s = " Trần Duy Thanh "
print(s, "=>", len(s))

s = ToiUuChuoi(s)
print(s, "=>", len(s))
