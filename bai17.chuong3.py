done = False
n, m= 0, 100
while not done and  n!=m:
    n = int(input('Nhap n: '))
    if n<0:
        print("n = ", n)
        break
    if n==m:
        break
    print("n = ", n)