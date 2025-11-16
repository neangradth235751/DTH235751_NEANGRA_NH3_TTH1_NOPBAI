def NhapVaSapXepGiamDan():
    print("\n--- Câu 8: Nhập Dãy Số và Sắp xếp Giảm Dần ---")
    day_so_M = []
    
    try:
        N = int(input("Nhập số phần tử N của dãy số M: "))
        if N <= 0:
            print("N phải là số nguyên dương.")
            return

        print(f"Bắt đầu nhập {N} số thực:")
        for i in range(N):
            while True:
                try:
                    # Nhập số thực (float)
                    so = float(input(f"Nhập M[{i}]: "))
                    day_so_M.append(so)
                    break
                except ValueError:
                    print("LỖI: Vui lòng nhập một số thực hợp lệ.")
        
        print("\nDãy số M đã nhập:")
        print(day_so_M)
        
        # Sắp xếp dãy số theo thứ tự giảm dần (reverse=True)
        day_so_M.sort(reverse=True) 
        
        print("Dãy số M sau khi sắp xếp GIẢM DẦN:")
        print(day_so_M)

    except ValueError:
        print("Lỗi: Số phần tử N không phải là số nguyên hợp lệ.")

# Chạy hàm
# NhapVaSapXepGiamDan()
