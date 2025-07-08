
print("--------------------- Mükemmel Sayı Bulma ---------------------")

# Mükemmel sayıyı kontrol eden fonksiyon
def mukBul(s):
    toplam = 0

    # 1'den s'e kadar olan sayıları kontrol et
    for i in range(1, s):
        # Eğer sayı i'ye tam olarak bölünüyorsa, i'yi toplama ekle
        if s % i == 0:
            toplam += i

    # Sayının mükemmel olup olmadığını kontrol et
    return toplam == s

# 1'den 1000'e kadar olan sayılar için mükemmel sayıları kontrol et
for i in range(1, 1001):
    if mukBul(i):
        print(i, "Mükemmel sayıdır.")
