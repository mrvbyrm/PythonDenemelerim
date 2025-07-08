print("*********-------- SONSUZ TOPLAM --------*********\n"
      "\n"
"Çıkmak için'e'ye basın\n")
toplam = 0
while True:
    sayı = input("Sayı gir:")
    if sayı=="e":
        print("Program sonlandırılıyor...")
        break
    sayı=int(sayı)
    toplam+=sayı
    print("Toplam=",toplam)

