def pisagor_bulma():
    """
    1'den 100'e kadar olan tam sayılar arasında Pythagorean üçlülerini bulan fonksiyon.

    Returns:
        list: Pythagorean üçlülerini içeren liste.
    """
    pisagor_listesi = []

    # İki döngü ile olası tüm kombinasyonları kontrol et
    for i in range(1, 101):
        for j in range(1, 101):
            # Hipotenüs hesaplama
            c = (i ** 2 + j ** 2) ** 0.5

            # Hipotenüs tam bir sayı ise, Pythagorean üçlüsü listeye ekle
            if c == int(c):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi

# Pythagorean üçlülerini bul ve ekrana yazdır
for i in pisagor_bulma():
    print(i)