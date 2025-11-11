from datetime import datetime, timedelta

# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

try:
    d = datetime(nam, thang, ngay)
    ngay_ke_tiep = d + timedelta(days=1)
    print("Ngày kế tiếp là: {}/{}/{}".format(ngay_ke_tiep.day, ngay_ke_tiep.month, ngay_ke_tiep.year))
except ValueError:
    print("Ngày không hợp lệ.")
