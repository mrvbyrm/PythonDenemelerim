print("""""""********Kullanıcı Giriş Programı********""""""")

sys_kullanıcı_adı="merve"
sys_kullanıcı_parola="12345"
giriş_hakkı=3

while True:
    kullanıcı_adı=input("Kullanıcı adı giriniz: ")
    kullanıcı_sifre=input("Kullanıcı şifresi giriniz: ")

    if kullanıcı_adı!=sys_kullanıcı_adı and kullanıcı_sifre==sys_kullanıcı_parola:
        print("Lütfen kullanıcı adını doğru giriniz!")
        giriş_hakkı-=1
        print("Kalan Giriş Hakkınız: ",giriş_hakkı)
    elif kullanıcı_adı==sys_kullanıcı_adı and kullanıcı_sifre!=sys_kullanıcı_parola:
        print("Lütfen kullanıcı şifresini doğru giriniz!")
        yeni_sifre=input("Parolanızı mı unuttunuz(evet/hayır): ")
        if(yeni_sifre=="hayır"):
            giriş_hakkı -= 1
            print("Kalan Giriş Hakkınız: ", giriş_hakkı)
        else:
            print("Mail adresinize şifreniz gönderilmiştir...")
            giriş_hakkı -= 1
            print("Kalan Giriş Hakkınız: ", giriş_hakkı)

    elif kullanıcı_adı!=sys_kullanıcı_adı and kullanıcı_sifre!=sys_kullanıcı_parola:
        print("Lütfen kullanıcı adını ve şifresini doğru giriniz!")
        giriş_hakkı-=1
        print("Kalan Giriş Hakkınız: ", giriş_hakkı)
    else:
        print("Hoşgeldiniz!Sisteme başarıyla giriş yapıldı...")
        break
    if(giriş_hakkı==0):
        print("Giriş Hakkınız Bitti...")
        break