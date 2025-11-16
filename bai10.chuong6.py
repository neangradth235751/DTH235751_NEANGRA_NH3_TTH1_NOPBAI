def NhapMaTranList(ten_ma_tran):
    """Nhập ma trận dưới dạng List lồng nhau."""
    while True:
        try:
            m = int(input(f"Nhập số dòng cho ma trận {ten_ma_tran}: "))
            n = int(input(f"Nhập số cột cho ma trận {ten_ma_tran}: "))
            if m <= 0 or n <= 0:
                print("Số dòng và số cột phải lớn hơn 0.")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên.")
            
    D = []
    print(f"Nhập các phần tử cho ma trận {ten_ma_tran} ({m}x{n}):")
    for i in range(m):
        row = []
        for j in range(n):
            while True:
                try:
                    val = float(input(f"Nhập phần tử {ten_ma_tran}[{i}][{j}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Lỗi: Vui lòng nhập số thực.")
        D.append(row)
    return D, m, n

def XuatMaTranList(D):
    """Xuất ma trận (List lồng nhau) ra màn hình."""
    for row in D:
        print('\t'.join(map(str, row)))

def CongHaiMaTranList(A, B, m, n):
    """Cộng hai ma trận List lồng nhau."""
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def TinhMaTranHoanViList(M, m, n):
    """Tính ma trận hoán vị (chuyển vị) của ma trận M."""
    # Kích thước ma trận chuyển vị là n x m
    M_T = [[0 for _ in range(m)] for _ in range(n)] 
    
    for i in range(m):
        for j in range(n):
            M_T[j][i] = M[i][j]
            
    return M_T

# --- Chương trình chính ---
# Nhập A
print("--- Nhập ma trận A ---")
A, m_A, n_A = NhapMaTranList("A")

# Nhập B
print("\n--- Nhập ma trận B ---")
B, m_B, n_B = NhapMaTranList("B")

print("\n--- Ma trận A và B đã nhập ---")
print("Ma trận A:")
XuatMaTranList(A)
print("Ma trận B:")
XuatMaTranList(B)

# 1. Cộng hai ma trận
print("\n--- Kết quả Cộng hai Ma trận A + B ---")
if m_A == m_B and n_A == n_B:
    Tong = CongHaiMaTranList(A, B, m_A, n_A)
    XuatMaTranList(Tong)
else:
    print("Lỗi: Không thể cộng hai ma trận có kích thước khác nhau.")

# 2. Tính ma trận hoán vị
print("\n--- Tính Ma trận Hoán vị (Chuyển vị) ---")

A_T = TinhMaTranHoanViList(A, m_A, n_A)
print("Ma trận hoán vị của A (A^T):")
XuatMaTranList(A_T)

B_T = TinhMaTranHoanViList(B, m_B, n_B)
print("Ma trận hoán vị của B (B^T):")
XuatMaTranList(B_T)
