def ToiUuChuoiDanhTu(s: str) -> str:
    """
    Tối ưu hóa chuỗi danh từ: loại bỏ khoảng trắng dư thừa, 
    viết hoa ký tự đầu tiên của mỗi từ.
    """
    # 1. Loại bỏ khoảng trắng ở hai đầu chuỗi và tách chuỗi thành danh sách các từ.
    #    split() mặc định sẽ tách chuỗi dựa trên bất kỳ chuỗi khoảng trắng nào 
    #    và loại bỏ các chuỗi rỗng kết quả (tối ưu hóa khoảng trắng dư thừa).
    words = s.strip().split() 
    
    # 2. Định dạng lại mỗi từ: chuyển tất cả thành chữ thường, sau đó viết hoa chữ cái đầu tiên (Title Case).
    optimized_words = [word.capitalize() for word in words]
    
    # 3. Nối các từ lại với nhau bằng một khoảng trắng duy nhất.
    return " ".join(optimized_words)

# --- Ví dụ kiểm tra ---
input_str = " TRẦN duY    thAnH  "
output_str = ToiUuChuoiDanhTu(input_str)

print(f"Input: \"{input_str}\"")
print(f"Output: \"{output_str}\"")

# Ví dụ khác
input_str_2 = "   nguYỄn văn  a "
output_str_2 = ToiUuChuoiDanhTu(input_str_2)
print(f"\nInput: \"{input_str_2}\"")
print(f"Output: \"{output_str_2}\"")
