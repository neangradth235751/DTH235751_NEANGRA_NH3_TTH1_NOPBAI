def CheckPrime(x):
    dem = 0
    # Số nguyên tố phải là số nguyên dương > 1
    if x <= 1:
        return False
        
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    # Số nguyên tố có chính xác 2 ước số (1 và chính nó)
    return dem == 2

s = "5;7;8;-2;8;11;-13;9;10"
# Tách chuỗi thành một danh sách (list) các chuỗi số
arr = s.split(';')

sochan = 0
soam = 0
sont = 0
sum_val = 0 # Đổi tên biến sum thành sum_val để tránh trùng với hàm built-in sum()

# Lặp qua từng phần tử trong danh sách arr
print("--- Danh sách các phần tử ---")
for x in arr:
    print(x)
    
    # Chuyển chuỗi số sang kiểu số nguyên
    number = int(x)
    
    # Kiểm tra số chẵn
    if number % 2 == 0:
        sochan += 1
        
    # Kiểm tra số âm
    if number < 0:
        soam += 1
        
    # Kiểm tra số nguyên tố
    # Lưu ý: Hàm CheckPrime(x) chỉ hoạt động đúng với số nguyên dương > 1.
    # Trong trường hợp này, các số âm trong chuỗi sẽ không được tính là SNT.
    if CheckPrime(number):
        sont += 1
        
    # Tính tổng
    sum_val = sum_val + number

# --- Kết quả ---
print("\n--- Kết quả Phân tích ---")
print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số Nguyên tố =", sont)

# Tính Trung bình Cộng: Tổng / Số lượng phần tử
if len(arr) > 0:
    trungbinh = sum_val / len(arr)
    print("Trung bình =", trungbinh)
else:
    print("Không có phần tử nào trong chuỗi để tính trung bình.")
