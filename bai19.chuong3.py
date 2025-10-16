import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = x  # Khởi đầu với x
for i in range(1, n + 1):
    mu = 2 * i + 1
    S += x ** mu / math.factorial(mu)

print("Giá trị S(x, n) =", S)