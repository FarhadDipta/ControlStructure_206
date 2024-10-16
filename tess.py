nilai1 = float(input("Masukan nilai ke-1 : "))
nilai2 = float(input("Masukan nilai ke-2 : "))
nilai3 = float(input("Masukan nilai ke-3 : "))

if nilai1 >= nilai2 and nilai1 >= nilai3 :
    print("Angka Terbesar adalah ",nilai1)
elif nilai2 >= nilai1 and nilai2 >= nilai3 : 
    print("Angka Terbesar adalah ",nilai2)
else :
    print("Angka Terbesar adalah ",nilai3)