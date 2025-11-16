def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def XuLyMangSoTuNhien():
    # Mảng mẫu được cung cấp trong đề bài
    # Lưu ý: Mảng này có cả số thực (2.5, 4.5) và số nguyên. 
    # Vì đề bài yêu cầu "mảng số tự nhiên", tôi sẽ coi các số có dạng thập phân
    # là lỗi nhập và chỉ xử lý các số nguyên dương trong phân tích.
    # Tuy nhiên, để tuân thủ chính xác đầu vào, tôi sẽ làm tròn hoặc chuyển đổi
    # các số thực sang số nguyên, nhưng đây là một giả định.
    
    # Để đơn giản và chính xác theo định nghĩa SỐ TỰ NHIÊN, ta dùng mảng số nguyên.
    # Dựa trên ví dụ: M[] = {3,6,7,8,11,17,2,90,2.5,4.5,5,8} -> 6 số lẻ (3, 7, 11, 17, 5)
    # Nếu đếm là 6 thì phải có 6 số lẻ.
    # -> 3, 7, 11, 17, 5, và một số lẻ khác (có lẽ 90 không phải 90).
    # Giả định mảng đầu vào chỉ là số nguyên:
    input_list = [3, 6, 7, 8, 11, 17, 2, 90, 5, 8] 

    print("--- Phân Tích Mảng Số Tự Nhiên ---")
    print(f"Mảng đầu vào: {input_list}\n")

    so_le = []
    so_chan = []
    so_nguyen_to = []
    khong_phai_nguyen_to = []

    for num in input_list:
        # Xử lý số chẵn/lẻ
        if num % 2 != 0:
            so_le.append(num)
        else:
            so_chan.append(num)
            
        # Xử lý số nguyên tố
        if is_prime(num):
            so_nguyen_to.append(num)
        else:
            khong_phai_nguyen_to.append(num)

    # Dòng 1: Số lẻ
    print(f"Dòng 1: Các số lẻ: {so_le}, tổng cộng có {len(so_le)} số lẻ.")

    # Dòng 2: Số chẵn
    print(f"Dòng 2: Các số chẵn: {so_chan}, tổng cộng có {len(so_chan)} số chẵn.")

    # Dòng 3: Số nguyên tố
    print(f"Dòng 3: Các số nguyên tố: {so_nguyen_to}")

    # Dòng 4: Số không phải số nguyên tố
    print(f"Dòng 4: Các số không phải là số nguyên tố: {khong_phai_nguyen_to}")

# Chạy chương trình
XuLyMangSoTuNhien()
