import random
import time

class Kumandaa:
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["TRT", "FOX TV", "Kanal D", "ATV", "STAR TV"], kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_Ac(self):
        if self.tv_durum == "Açık":
            print("TV zaten açık...")
        else:
            print("TV açılıyor...")
            self.tv_durum = "Açık"

    def tv_Kapat(self):
        if self.tv_durum == "Kapalı":
            print("TV kapanıyor...")
            self.tv_durum = "Kapalı"
        else:
            print("TV zaten kapalı...")

    def ses_Ayarları(self):
        while True:
            cevap = input("Sesi azalt = '<'\nSesi Artır = '>'\nÇıkış = 'e'")
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses Seviyesi : ", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 100:
                    self.tv_ses += 1
                    print("Ses Seviyesi : ", self.tv_ses)
            elif cevap == "e":
                print("Ses Güncellendi Çıkış Yapılıyor...")
                break
            else:
                print("Hatalı tuşlama yaptınız...")
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal : ", self.kanal)

    def kanal_sayisi(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV Durumu : {}\nTV Ses Seviyesi : {}\nKanal Listesi : {}\nŞu anki Kanal : {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)


print("""
TELEVİZYON UYGULAMASI
1. TV Aç
2. TV Kapa
3. Ses Seviyesi Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri

Çıkmak için 'e' ye basın""")

kumanda = Kumandaa()  # Kumanda sınıfından bir nesne oluşturulmalı

while True:
    işlem = input("İşlemi Seçin: ")

    if işlem == "e":
        print("Çıkış yaptınız...")
        break
    elif işlem == "1":
        kumanda.tv_Ac()
    elif işlem == "2":
        kumanda.tv_Kapat()
    elif işlem == "3":
        kumanda.ses_Ayarları()
    elif işlem == "4":
        kanal_ismi = input("Eklemek istediğiniz kanal isimlerini ',' ile ayırarak girin : ")
        kanal_listesi=kanal_ismi.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem == "5":
        print("Kanal Sayısı:", kumanda.kanal_sayisi())
    elif işlem == "6":
        kumanda.rastgele_kanal()
    elif işlem == "7":
        print(kumanda)
    else:
        print("Hatalı tuşlama yaptınız.")
        break
