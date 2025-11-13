from random import randrange

print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))

# Khởi tạo List ngẫu nhiên
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)

print("List ngẫu nhiên là:")
print(lst)

# Thêm phần tử mới
print("Mời bạn thêm số mới:")
value = int(input())
lst.append(value)
print(lst)

# Đếm số lần xuất hiện
print("Bạn muốn đếm số nào:")
k = int(input())
dem = lst.count(k)
print(k, "xuất hiện ", dem, " lần trong list")

# Định nghĩa hàm kiểm tra số nguyên tố
def CheckPrime(n):
    d = 0
    # Số nguyên tố phải là số nguyên dương > 1
    if n <= 1:
        return False
        
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2

# Xử lý số nguyên tố trong list
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có ", demnt, " số nguyên tố trong list")
print("Tổng các số nguyên tố =", tongnt)

# Sắp xếp list
lst.sort()
print("List sau khi sort:")
print(lst)

# Xóa list (xóa tham chiếu biến)
del lst
print("List sau khi xóa:")
# Lệnh print(lst) sau khi del lst sẽ gây lỗi NameError vì biến không còn tồn tại
# Tuy nhiên, để giữ nguyên logic của đề bài, ta giữ lại lệnh này 
# (người dùng sẽ thấy lỗi nếu chạy)
# print(lst)
