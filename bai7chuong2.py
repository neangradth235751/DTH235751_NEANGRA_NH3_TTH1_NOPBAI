'''
1. Dùng hàm input()
Đây là cách cơ bản nhất để nhập dữ liệu từ người dùng.

Dữ liệu nhập vào luôn ở dạng chuỗi (str).

Ví dụ:

ten = input("Nhập tên của bạn: ")
print("Xin chào,", ten)

 2. Ép kiểu dữ liệu khi nhập
Vì input() trả về chuỗi, nên cần ép kiểu nếu muốn xử lý số.

Ví dụ:

tuoi = int(input("Nhập tuổi của bạn: "))  # ép kiểu sang int
diem = float(input("Nhập điểm trung bình: "))  # ép kiểu sang float

3. Nhập nhiều giá trị cùng lúc
Dùng split() để tách các giá trị nhập cùng một dòng.

Ví dụ:

a, b = input("Nhập hai số cách nhau bởi dấu cách: ").split()
a = int(a)
b = int(b)
print("Tổng =", a + b)
Hoặc gọn hơn:

a, b = map(int, input("Nhập hai số: ").split())
 4. Dùng vòng lặp để nhập nhiều dòng
 Ví dụ:

n = int(input("Nhập số lượng phần tử: "))
ds = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i+1}: ")
    ds.append(x)
print("Danh sách đã nhập:", ds)


'''