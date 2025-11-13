from random import randrange

lst = []
print("Nhập số phần tử:")
n = int(input())

# Khởi tạo List ngẫu nhiên
for i in range(n):
    lst.append(randrange(0, 100))

print("List sau khi tạo ngẫu nhiên là:")
print(lst)

# Thêm phần tử mới
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# Xóa tất cả các lần xuất hiện của một số
k = int(input("Mời nhập số để xóa: "))
while lst.count(k) > 0:
    lst.remove(k)

print("List sau khi xóa:")
print(lst)

# Định nghĩa hàm kiểm tra đối xứng
def CheckDoiXung(lst):
    for i in range(len(lst)):
        # So sánh phần tử thứ i từ đầu với phần tử thứ i từ cuối
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

# Kiểm tra và in kết quả đối xứng
kt = CheckDoiXung(lst)
if kt == True:
    print("List đối xứng")
else:
    print("List không đối xứng")
