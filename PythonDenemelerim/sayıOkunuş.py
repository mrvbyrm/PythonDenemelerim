def okunus(sayi):
    """
    Belirtilen bir sayının okunuşunu hesaplayan fonksiyon.

    Args:
        sayi (int): Okunuşu hesaplanacak sayı.

    Returns:
        str: Sayının okunuşu.
    """
    birinci = sayi % 10
    ikinci = sayi // 10
    return onlar[ikinci] + " " + birler[birinci]
def sayiyi_okunus_ile_yazdir():
    """
    Kullanıcıdan bir sayı alır, sayının geçerli bir aralıkta olup olmadığını kontrol eder
    ve sayının okunuşunu ekrana yazdırır.
    """
    sayi = int(input("Sayı girin: "))

    # Sayının 0 ile 99 arasında olup olmadığını kontrol et
    if sayi < 0 or sayi > 99:
        print("Lütfen 0 ile 99 arasında bir sayı girin.")
    elif sayi == 0:
        print("Sıfır")
    else:
        print("Okunuş:", okunus(sayi))
if __name__ == "__main__":
    # Birler ve onlar basamağı için okunuşları içeren listeler
    birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    print("*************-------- Sayıların Okunuşu --------*************")
    sayiyi_okunus_ile_yazdir()