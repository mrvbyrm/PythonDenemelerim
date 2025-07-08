class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller
    def bilgileriGöster(self):
        print("""
        Yazılımcı Objesinin Özellikleri\n
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Bildiği Diller : {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def zam_Yap(self,zam_miktarı):
        print("Zam Yapılıyor...")
        self.maaş+=zam_miktarı
    def dil_Ekle(self,yeni_dil):
        print("Dil Ekleniyor...")
        self.diller.append(yeni_dil)
        yazılımcı = Yazılımcı("Merve", "Bayram", 12345, 60000, ["Python", "Java", "C", "C#"])
        yazılımcı.bilgileriGöster()
        yazılımcı.dil_Ekle("Javascript")
        yazılımcı.zam_Yap(1000)
        yazılımcı.bilgileriGöster()