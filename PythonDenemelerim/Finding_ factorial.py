print("-----------------------------------------------------------\n"
      "FAKTORİYEL BULMA\n\n"
      "Çıkmak için 'e'ye basın!\n"
      "-------------------------------------------------------------\n")

while True:
    sayı=input("Faktöriyelini almak istediğiniz sayıyı girin:")
    if(sayı=="e"):
        print("Başarıyla çıkış yaptınız...")
        break
    else:
        sayı=int(sayı)
        faktoriyel=1
        print("Faktöriyelini almak istediğiniz 'sayı':",sayı)
        for i in range(2,sayı+1):
            faktoriyel*=i
        print("Faktöriyel=", faktoriyel)
