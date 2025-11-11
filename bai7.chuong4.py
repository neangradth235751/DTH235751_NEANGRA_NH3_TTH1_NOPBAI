import math

# Nhập tọa độ điểm A và B
xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))
xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))

# Tính độ dài đoạn thẳng AB
dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Xuất kết quả
print(f"Độ dài đoạn thẳng AB là: {dAB}")
