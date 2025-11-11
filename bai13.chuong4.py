def sum_of_divisors(n: int) -> int:
    """
    Tính tổng các ước số riêng (ước số khác n) của số nguyên dương n.
    
    Args:
        n: Số nguyên dương cần tính tổng ước.
        
    Returns:
        Tổng các ước số riêng của n.
    """
    if n <= 0:
        return 0
    
    total = 0
    # Các ước số nằm trong khoảng từ 1 đến căn bậc hai của n
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisor1 = i
            divisor2 = n // i
            
            # Ước số thứ nhất (i)
            total += divisor1
            
            # Ước số thứ hai (n // i)
            # Kiểm tra để tránh cộng ước số n (n // 1) và tránh cộng 
            # hai lần khi n là số chính phương (i == n // i)
            if divisor1 != divisor2 and divisor2 != n:
                total += divisor2
            
            # Trường hợp đặc biệt: Nếu i là 1, ta đã cộng 1. 
            # Ước số thứ hai là n, mà ta không tính, nên ta xử lý bằng điều kiện trên.
            # Với i=1, divisor2=n. Ta phải đảm bảo không cộng n.
            # Với n=6: i=1 (total+=1, divisor2=6). Ta không cộng 6. total=1
            #           i=2 (total+=2, divisor2=3). Ta cộng 3. total=1+2+3=6
            
        i += 1
        
    # Vì thuật toán trên cộng luôn ước số 1 (khi i=1), và ta cần loại trừ ước số n.
    # Ta phải loại bỏ ước số n nếu n > 1. 
    # Do cách xử lý ước số thứ hai ở trên đã loại trừ n (if divisor2 != n), 
    # tổng 'total' hiện tại đã là tổng ước số riêng.
    
    return total

# --- Yêu cầu a) Kiểm tra số hoàn thiện (Perfect number) ---

def is_perfect_number(n: int) -> bool:
    """
    Kiểm tra số nguyên dương n có phải là số hoàn thiện hay không.
    Số hoàn thiện là số có tổng các ước số riêng bằng chính nó.
    """
    if n <= 1:
        return False
        
    return sum_of_divisors(n) == n

# --- Yêu cầu b) Kiểm tra số thịnh vượng (Abundant number) ---

def is_abundant_number(n: int) -> bool:
    """
    Kiểm tra số nguyên dương n có phải là số thịnh vượng hay không.
    Số thịnh vượng là số có tổng các ước số riêng lớn hơn nó.
    """
    if n <= 0:
        return False
        
    return sum_of_divisors(n) > n

# --- Ví dụ kiểm tra ---
print("--- Kiểm tra Số Hoàn Thiện (Perfect Number) ---")
n1 = 6
print(f"Tổng ước số riêng của {n1}: {sum_of_divisors(n1)}")
print(f"{n1} là số hoàn thiện? {is_perfect_number(n1)}") # Kết quả: True (1+2+3=6)

n2 = 28
print(f"Tổng ước số riêng của {n2}: {sum_of_divisors(n2)}")
print(f"{n2} là số hoàn thiện? {is_perfect_number(n2)}") # Kết quả: True (1+2+4+7+14=28)

n3 = 10
print(f"Tổng ước số riêng của {n3}: {sum_of_divisors(n3)}")
print(f"{n3} là số hoàn thiện? {is_perfect_number(n3)}") # Kết quả: False (1+2+5=8)

print("\n--- Kiểm tra Số Thịnh Vượng (Abundant Number) ---")
n4 = 12
print(f"Tổng ước số riêng của {n4}: {sum_of_divisors(n4)}")
print(f"{n4} là số thịnh vượng? {is_abundant_number(n4)}") # Kết quả: True (1+2+3+4+6=16 > 12)

n5 = 20
print(f"Tổng ước số riêng của {n5}: {sum_of_divisors(n5)}")
print(f"{n5} là số thịnh vượng? {is_abundant_number(n5)}") # Kết quả: True (1+2+4+5+10=22 > 20)

n6 = 9
print(f"Tổng ước số riêng của {n6}: {sum_of_divisors(n6)}")
print(f"{n6} là số thịnh vượng? {is_abundant_number(n6)}") # Kết quả: False (1+3=4 < 9)
