# Başlık ve çıkış talimatı yazdırılır
print("******************------------------- ASAL SAYI BULMA -------------------******************")
print("Çıkmak için 'e'ye basın!")

# Bir sayının asal olup olmadığını kontrol eden fonksiyon
def asalSayıMı(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        # 2'den x'e kadar olan sayıları kontrol et
        for i in range(2, x):
            # Eğer x'i i'ye tam bölen bir sayı varsa, x asal değildir
            if x % i == 0:
                return False
        # Hiçbir sayıya tam olarak bölünmüyorsa, x asal bir sayıdır
        return True

# Ana döngü
while True:
    # Kullanıcıdan bir sayı istenir
    sayı = input("Bir sayı girin: ")

    # Eğer kullanıcı 'e' tuşuna bastıysa çıkış yapılır
    if sayı == "e":
        print("Başarıyla çıkış yaptınız...")
        break
    else:
        # Girilen değer sayıya dönüştürülür
        sayı = int(sayı)

        # asalSayıMı fonksiyonu kullanılarak sayının asal olup olmadığı kontrol edilir
        if asalSayıMı(sayı):
            print(sayı, "Sayı asal sayıdır.")
        else:
            print(sayı, "Sayı asal değildir.")
