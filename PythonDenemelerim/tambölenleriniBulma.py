# Başlık ve çıkış talimatı yazdırılır
print("*****------*****---- Tam Bölenlerini Bulma ----*****------*****")
print("\nÇıkmak için q'ya basın!")

# Bir sayının tam bölenlerini bulan fonksiyon
def tambolenleriniBulma(s):
    tam_bolenler = []  # Tam bölenleri saklamak için boş bir liste oluşturulur

    for i in range(1, s + 1):  # 1'den sayıya kadar olan sayıları kontrol et
        if s % i == 0:  # Eğer sayı i'ye tam olarak bölünüyorsa
            tam_bolenler.append(i)  # Tam bölen listesine i'yi ekle

    return tam_bolenler  # Tam bölenleri içeren liste döndürülür

while True:
    sayı = input("Bir sayı girin: ")

    # Kullanıcı 'q' tuşuna bastığında programdan çıkılır
    if sayı == "q":
        print("Program sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        # Sonucu yazdır
        print(sayı, "sayısının tam bölenleri:", tambolenleriniBulma(sayı))