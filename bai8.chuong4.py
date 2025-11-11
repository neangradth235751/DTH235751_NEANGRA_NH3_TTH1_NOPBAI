# log_base.py
import math

def read_float(prompt):
    """Đọc một số thực từ input, lặp lại nếu người dùng nhập không đúng."""
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập một số thực.")

def main():
    print("Tính log_a(x) = ln(x) / ln(a)")
    # Nhập x
    x = read_float("Nhập x (x > 0): ")
    while x <= 0:
        print("x phải lớn hơn 0.")
        x = read_float("Nhập x (x > 0): ")

    # Nhập a
    a = read_float("Nhập a (a > 0 và a != 1): ")
    while a <= 0 or a == 1.0:
        if a <= 0:
            print("a phải lớn hơn 0.")
        else:
            print("a không được bằng 1.")
        a = read_float("Nhập a (a > 0 và a != 1): ")

    # Tính log cơ số a của x
    # Cách 1: dùng ln (an toàn)
    try:
        result = math.log(x) / math.log(a)
    except ValueError as e:
        print("Lỗi trong quá trình tính toán:", e)
        return

    # Hoặc có thể dùng math.log(x, a) (Python hỗ trợ)
    # result = math.log(x, a)

    # Xuất kết quả (làm tròn 6 chữ số thập phân)
    print(f"\nKết quả: log_{a}({x}) = {result:.6f}")

if __name__ == "__main__":
    main()
