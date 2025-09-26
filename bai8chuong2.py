'''

1. Lỗi cú pháp (SyntaxError)
Xảy ra khi bạn viết sai quy tắc ngữ pháp của Python.

Ví dụ: quên dấu : ở cuối dòng if, thiếu dấu ngoặc.

if x > 5  # thiếu dấu :
    print("Lỗi cú pháp")
2. Lỗi kiểu dữ liệu (TypeError)
Khi bạn thực hiện phép toán hoặc thao tác không hợp lệ với kiểu dữ liệu.

x = "5"
y = x + 2  # lỗi vì không thể cộng chuỗi với số
3. Lỗi giá trị (ValueError)
Khi bạn truyền giá trị không hợp lệ cho một hàm.

int("abc")  # không thể chuyển chuỗi "abc" thành số nguyên
4. Lỗi tên biến (NameError)
Khi bạn gọi một biến chưa được định nghĩa.

print(score)  # chưa khai báo biến score
5. Lỗi chia cho 0 (ZeroDivisionError)
Khi bạn chia một số cho 0.

x = 10 / 0  # lỗi chia cho 0
6. Lỗi chỉ số (IndexError)
Khi bạn truy cập phần tử ngoài phạm vi của danh sách.

lst = [1, 2, 3]
print(lst[5])  # chỉ số 5 không tồn tại
 Cách bắt lỗi trong Python: dùng try...except
Cấu trúc:

try:
    # đoạn mã có thể gây lỗi
except LoaiLoi:
    # xử lý khi lỗi xảy ra
 Ví dụ:

try:
    x = int(input("Nhập số nguyên: "))
    print("Bạn vừa nhập:", x)
except ValueError:
    print("Lỗi! Bạn phải nhập số nguyên.")
Có thể dùng nhiều khối except để xử lý từng loại lỗi:

try:
    x = int(input("Nhập số: "))
    y = 10 / x
except ValueError:
    print("Giá trị không hợp lệ!")
except ZeroDivisionError:
    print("Không thể chia cho 0!")
Dùng finally để thực hiện hành động cuối cùng (dù có lỗi hay không):

try:
    print("Thực hiện phép chia")
    result = 10 / 2
except:
    print("Có lỗi xảy ra")
finally:
    print("Kết thúc chương trình")


'''