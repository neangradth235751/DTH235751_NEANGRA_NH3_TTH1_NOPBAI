thang = int(input("Nhập vào tháng (1-12): "))

if 1 <= thang <= 3:
    print(f"Tháng {thang} thuộc quý 1.")
elif 4 <= thang <= 6:
    print(f"Tháng {thang} thuộc quý 2.")
elif 7 <= thang <= 9:
    print(f"Tháng {thang} thuộc quý 3.")
elif 10 <= thang <= 12:
    print(f"Tháng {thang} thuộc quý 4.")
else:
    print("Tháng không hợp lệ.")