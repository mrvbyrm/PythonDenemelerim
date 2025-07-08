import random
import time

print("""*******************************************-----------------------------
      Sayı Tahmin Oyunu
      1 ile 40 arasında olan sayıyı tahmin edin.
-----------------------------*******************************************""")
#dir(random)
#help(random)
rastgele_sayı=random.randint(1,40)
tahmin_hakkı=7

while True:
    tahmin=int(input("Tahmininiz:"))
    if(tahmin>=40):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Lütfen 1-40 arasında bir sayı giriniz")
    elif(tahmin<=1):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Lütfen 1-40 arasında bir sayı giriniz")
    else:
        if (tahmin < rastgele_sayı):
            print("Bilgiler Sorgulanıyor...")
            time.sleep(1)

            print("Daha büyük bir sayı söyleyin!")
            tahmin_hakkı -= 1
            print("Kalan Tahmin Hakkı:", tahmin_hakkı)
        elif (tahmin > rastgele_sayı):
            print("Bilgiler Sorgulanıyor...")
            time.sleep(1)
            print("Daha küçük bir sayı söyleyin!")
            tahmin_hakkı -= 1
            print("Kalan Tahmin Hakkı:", tahmin_hakkı)
        else:
            print("Bilgiler Sorgulanıyor...")
            time.sleep(1)
            print("Tebrikler!Sayımız:", rastgele_sayı)
            break
        if (tahmin_hakkı == 0):
            print("Tahmin hakkınız bitti!")
            print("Sayımız:", rastgele_sayı)
            break
