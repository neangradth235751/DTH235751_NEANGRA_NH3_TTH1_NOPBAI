def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return don_vi[n] if n != 0 else "không"
    elif n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + (don_vi[n % 10] if n % 10 != 5 else "lăm")
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hang_chuc[chuc]
        elif dv == 1:
            return hang_chuc[chuc] + " mốt"
        elif dv == 5:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + don_vi[dv]

n = int(input("Nhập số n (tối đa 2 chữ số): "))
if 0 <= n <= 99:
    print(doc_so(n).capitalize())
else:
    print("Vui lòng nhập số có tối đa 2 chữ số.")