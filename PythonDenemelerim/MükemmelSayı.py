print("--------------------- Mükemmel Sayı Bulma ---------------------")
sayı=int(input("Sayıyı girin:"))
if sayı <= 0:
    print("Lütfen pozitif bir sayı girin.")
else:
    toplam=0
    for i in range(1,sayı):
        if(sayı%i==0):
            toplam+=i
    if(toplam==sayı):
        print("{} sayısı mükemmel sayıdır.".format(sayı))
    else:
        print("{} sayısı mükemmel sayı değildir.".format(sayı))