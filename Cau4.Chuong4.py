def ROI (dt,cp):
    return (dt-cp)/cp
def GoiYDauTu (roi):
    if roi>0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đàu tư"
print("Chương trình tính ROI")
dt=int(input("Nhập Doanh Thu: "))
cp=int(input("NHập chi phí: "))
roi=ROI(dt,cp)
print("Tỉ lệ ROI= ",roi)
print("==>",GoiYDauTu(roi))

    