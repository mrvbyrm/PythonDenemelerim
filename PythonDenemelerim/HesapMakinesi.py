import math
import time
print("""**************--------************** HESAP MAKİNESİ **************--------************** 
1-TOPLAMA                (+)
2-ÇIKARMA                (-)
3-ÇARPMA                 (x) 
4-BÖLME                  (/)
5-KAREKÖK ALMA           (½)
6-KARE ALMA              (^2)
7-ÜS ALMA                (^n)
8-LOGARİTMA HESAPLAMA    (log)
9-DERECEYİ RADYANA ÇEVİR  (π)
0-ÇIKIŞ   
""")

while True:
    seçim = int(input("Yapmak istediğiniz işlem:"))
    if(seçim==1):
        print("Seçiminiz: 1-TOPLAMA (+)")
        s1=int(input("1.sayıyı girin:"))
        s2 = int(input("2.sayıyı girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=",s1+s2)
    elif (seçim == 2):
        print("Seçiminiz: 2-TOPLAMA (-)")
        s1 = int(input("1.sayıyı girin:"))
        s2 = int(input("2.sayıyı girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", s1-s2)
    elif (seçim == 3):
        print("Seçiminiz: 3-ÇARPMA (x)")
        s1 = int(input("1.sayıyı girin:"))
        s2 = int(input("2.sayıyı girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", s1*s2)
    elif (seçim == 4):
        print("Seçiminiz: 4-BÖLME (/)")
        s1 = int(input("1.sayıyı girin:"))
        while True:
            s2 = int(input("2.sayıyı girin(0'dan farklı):"))
            if (s2 != 0):
                break
            else:
                print("Bölen sıfır olamaz! Tekrar sayı girin.")
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", s1 / s2)
    elif(seçim==5):
        print("Seçiminiz: 5-KAREKÖK ALMA (½)")
        s1 = int(input("Sayıyı girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", math.sqrt(s1))
    elif (seçim == 6):
        print("Seçiminiz: 6-KARESİNİ ALMA (^)")
        s1 = int(input("Sayıyı girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", math.pow(s1,2))
    elif (seçim == 7):
        print("Seçiminiz: 7-ÜS ALMA (^)")
        s1 = int(input("Sayıyı girin:"))
        s2 = int(input("Üssünü girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", math.pow(s1,s2))
    elif (seçim == 8):
        print("Seçiminiz: 8-LOGARİTMA HESAPLAMA (logn)")
        s1 = int(input("Sayıyı(n) girin:"))
        s2 = int(input("Taban girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", math.log(s1,s2))
    elif (seçim == 9):
        print("Seçiminiz: 9-DERECEYİ RADYANA ÇEVİR (π)")
        s1 = int(input("Sayıyı girin:"))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Sonuç=", math.degrees(s1))
    elif (seçim == 0):
        print("Seçiminiz: 0-ÇIKIŞ")
        print("İşleminiz sonlandırılıyor...")
        time.sleep(2)
        print("Tekrar bekleriz ... ")
        break
    else:
        print("Hatalı seçim yaptınız!")