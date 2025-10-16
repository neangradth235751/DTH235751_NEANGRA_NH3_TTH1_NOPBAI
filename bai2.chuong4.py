from random import randrange
while True:
 somay=randrange(1,101)
 solandoan=0
 win=False
 while solandoan<7:
   solandoan+=1
   songuoi=int(input("Máy đoán [1..100], mời bạn đoán:"))
   print("Bạn đoán lần thứ ",solandoan)
   if somay==songuoi:
       print("Chúc mừng bạn đoán đúng, số máy là=",somay)
       win=True
       break
   if somay>songuoi:
       print("Bạn đoán sai, số máy > số bạn")
   elif somay<songuoi:
       print("Bạn đoán sai, số máy < số bạn")
   if win==False:
       print("GAME OVER!, số máy =",somay)
   hoi=input("Tiếp không?")
   if hoi=="k":
       break
 if win==False:
    print("GAME OVER!, số máy =",somay)
 hoi=input("Tiếp không?")
 if hoi=="k":
     break
print("Cám ơn bạn đã chơi Game!")