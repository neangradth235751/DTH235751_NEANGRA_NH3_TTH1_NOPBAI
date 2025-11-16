from random import sample

def TaoListKhongTrungNhau():
    print("--- Câu 6: Tạo List không trùng nhau ---")
    try:
        N = int(input("Nhập số phần tử N cần tạo: "))
        if N <= 0:
            print("N phải là số nguyên dương.")
            return

        # Phạm vi ngẫu nhiên (ví dụ: từ 1 đến 2 * N để đảm bảo có đủ số không trùng)
        upper_limit = N * 2
        if N > upper_limit:
            print(f"Không thể tạo {N} số không trùng trong phạm vi {upper_limit}!")
            return

        # Dùng random.sample để chọn N phần tử không trùng lặp từ phạm vi [1, upper_limit]
        list_khong_trung = sample(range(1, upper_limit + 1), N)

        print(f"List {N} số ngẫu nhiên KHÔNG TRÙNG NHAU trong phạm vi [1, {upper_limit}] là:")
        print(list_khong_trung)

    except ValueError:
        print("Lỗi: Đầu vào không phải là số nguyên hợp lệ.")

# Chạy hàm
# TaoListKhongTrungNhau()
