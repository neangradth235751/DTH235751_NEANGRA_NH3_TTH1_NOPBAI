import math

# Nhập n
n = int(input("Nhập số n (số dấu căn lồng nhau): "))

# Biến S dùng để lưu giá trị căn lồng nhau
S = 0

# Tính từ trong ra ngoài
for i in range(n):
    S = math.sqrt(2 + S)

# Xuất kết quả
print(f"S({n}) = {S}")
