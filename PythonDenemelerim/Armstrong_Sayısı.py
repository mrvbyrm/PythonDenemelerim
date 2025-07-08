print("------------------Armstrong Sayısı---------------")

# Kullanıcıdan bir sayı girişi alınır ve 'sayı' değişkenine saklanır
sayı = input("Sayı girin:")

# Girilen sayının kaç basamaklı olduğunu hesaplamak için len() fonksiyonu kullanılır
basamak_sayisi = len(sayı)

# Girilen sayıyı bir tamsayıya dönüştürme işlemi
sayı = int(sayı)

# Değişkenlerin başlangıç değerleri atanır
basamak = 0
toplam = 0
temp = sayı

# Sayının basamaklarını işlemek için bir while döngüsü kullanılır
while temp > 0:
    # En sağdaki basamağı alır
    basamak = temp % 10

    # Toplam, her basamağın belirtilen üssü ile güncellenir
    toplam += basamak ** basamak_sayisi

    # En sağdaki basamağı atlar ve bir önceki basamağa geçer
    temp //= 10

# Girilen sayı ile hesaplanan toplam değeri karşılaştırılır
if toplam == sayı:
    print(sayı, "bir Armstrong sayısıdır.")
else:
    print(sayı, "bir Armstrong sayısı değildir.")
