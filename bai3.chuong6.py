from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

def LayDong(r):
    # D là ma trận toàn cục được tạo sau
    # Do đó, hàm này phải sử dụng D được định nghĩa ở ngoài
    # Hoặc ta sẽ truyền D vào như một đối số: def LayDong(D, r):
    # Giữ nguyên theo cấu trúc của bạn, dựa vào biến toàn cục D
    global D 
    R = D[r]
    return R

def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print() # Thêm xuống dòng sau khi xuất list

def LayCot(c):
    # Tương tự, dựa vào biến toàn cục D
    global D
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def MAX(D):
    # Khởi tạo max bằng phần tử đầu tiên của ma trận
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if(max_val < D[i][j]):
                max_val = D[i][j]
    return max_val

# --- Chương trình chính ---
print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

# Tạo ma trận D
D = TaoMaTran(m, n)
print("--- Ma trận ngẫu nhiên D ---")
XuatMaTran(D)

# Lấy và xuất dòng
print("Mời bạn nhập dòng muốn xuất (Bắt đầu từ 0):")
r = int(input())
print(f"Dòng {r} là:")
XuatList1Chieu(LayDong(r))

# Lấy và xuất cột
print("Mời bạn nhập cột muốn xuất (Bắt đầu từ 0):")
c = int(input())
print(f"Cột {c} là:")
XuatList1Chieu(LayCot(c))

# Tìm và xuất MAX
max_val = MAX(D)
print("Số lớn nhất trong ma trận =", max_val)
