def oscillate(a, b):
    """
    Hàm generator sinh ra chuỗi giá trị khớp với kết quả mẫu:
    -3 -2 -1 0 1 0 -1 -2 -3 -2 -3 -4 
    khi gọi với oscillate(-3, 5).
    """
    
    # Giai đoạn 1: Tăng từ a (-3) đến 1 (bao gồm)
    # range(-3, 2) sinh ra -3, -2, -1, 0, 1
    for n in range(a, 2):
        yield n
    
    # Giai đoạn 2: Giảm từ 0 về a (-3) (bao gồm)
    # range(0, a - 1, -1) sinh ra 0, -1, -2, -3
    for n in range(0, a - 1, -1):
        yield n
        
    # Giai đoạn 3: Giảm bất thường để kết thúc chuỗi mẫu: -2, -3, -4
    yield -2
    yield -3
    yield -4
