print("Değer Değiştirme")

s1=int(input("1.sayı girin:"))
s2=int(input("2.sayı girin:"))

print("İlk durumda 1.Sayı:",s1)
print("İlk durumda 2.Sayı:",s2)

s1,s2=s2,s1
print("Değerler Değiştirildikten Sonra:")
print("1.Sayı:",s1)
print("2.Sayı:",s2)