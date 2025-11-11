# Câu 5: Xử lý chuỗi với các hàm cơ bản

s = input("Nhập chuỗi: ")

hoa = thuong = so = ktdb = space = nguyen_am = phu_am = 0
nguyen_am_set = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1
    if ch.isdigit():
        so += 1
    elif not ch.isalnum() and not ch.isspace():
        ktdb += 1
    if ch.isspace():
        space += 1
    if ch.isalpha():
        if ch in nguyen_am_set:
            nguyen_am += 1
        else:
            phu_am += 1

print("Chữ IN HOA:", hoa)
print("Chữ in thường:", thuong)
print("Chữ là chữ số:", so)
print("Ký tự đặc biệt:", ktdb)
print("Khoảng trắng:", space)
print("Nguyên âm:", nguyen_am)
print("Phụ âm:", phu_am)
