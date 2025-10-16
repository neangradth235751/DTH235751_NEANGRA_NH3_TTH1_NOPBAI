n = int(input("Nhập chiều cao n: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)  # Dòng đầu và cuối: in toàn bộ dấu *
    else:
        print("* " + "  " * (n - 2) + "*")  # Dòng giữa: chỉ in dấu * ở hai đầu



n = int(input("Nhập chiều cao n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


n = int(input("Nhập chiều cao n: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == i or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()