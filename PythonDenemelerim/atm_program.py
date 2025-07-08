print("***************************  ATM Makinesine Hoşgeldiniz  *************************** \n"
"--------------------------------------------------\n"
"İşlemler\n"
"--------------------------------------------------\n"
"1.Bakiye Sorgulama\n"
"2.Para Çekme\n"
"3.Para Yatırma\n"
"Programdan çıkmak için 'e'ye basın...\n"
"************************************************************************************\n")

bakiye=1000

while True:
    işlem=input("Yapmak istediğiniz işlemi girin: ")
    if(işlem=="1"):
        print("1-Yapmak İstediğiniz İşlem:Bakiye Sorgulama")
        print("Bakiyeniz: ",bakiye,"TL")
    elif(işlem=="e"):
        print("Başarıyla çıkış yaptınız...Sizi Yine Bekleriz!")
        break
    elif(işlem=="2"):
        print("Yapmak İstediğiniz İşlem:2-Para Çekme")
        çekilecek_tutar = int(input("Çekmek istediğiniz tutarı girin: "))
        if(çekilecek_tutar<=bakiye):
            bakiye-=çekilecek_tutar
            print("İşleminiz Başarıyla Gerçekleşti...Kalan Bakiyeniz:",bakiye,"TL")
        else:
            print("Yeterli Bakiyeniz Bulunmamaktadır!")
            continue
    elif(işlem=="3"):
        print("Yapmak İstediğiniz İşlem:3-Para Yatırma")
        yatırılacak_tutar = int(input("Yatırmak istediğiniz tutarı girin: "))
        bakiye+=yatırılacak_tutar
        print("İşleminiz Başarıyla Gerçekleşti...Hesabınızdaki Bakiye:",bakiye,"TL")
    else:
        print("Hatalı Tuşlama Yaptınız...Lütfen Tekrar Deneyin!")
        continue