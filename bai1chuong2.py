import math
try:
    r=float(input("Moi ban nhap ban kinh tron:"))
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi =",cv)
    print("Dien tich=",dt)
excepct:
    print("Loi roi!")
