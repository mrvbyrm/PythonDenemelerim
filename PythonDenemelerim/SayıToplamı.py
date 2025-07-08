toplam = 0
while True:
    sayı = int(input("Sayı girin (Çıkmak için 0'a basın):"))
    if sayı== 0:
        print("Program Sonlandırılıyor...")
        break
    toplam += sayı
    print("Girdiğiniz Sayıların Toplamı:", toplam)