a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phep_toan = input("Nhập phép toán (+, -, *, /): ")

if phep_toan == "+":
    ket_qua = a + b
elif phep_toan == "-":
    ket_qua = a - b
elif phep_toan == "*":
    ket_qua = a * b
elif phep_toan == "/":
    if b != 0:
        ket_qua = a / b
    else:
        ket_qua = "Không thể chia cho 0."
else:
    ket_qua = "Phép toán không hợp lệ."

print("Kết quả:", ket_qua)