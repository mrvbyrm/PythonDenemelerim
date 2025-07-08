print("Fibonacci Serisi")  #1 1 2 3 5 8 13 21 34 55....
a=1
b=1
fibonacci=[a,b]
sayı=int(input("Hesaplamak istediğiniz fibonacci değerini girin:"))
for i in range(sayı):
    a,b=b,a+b
    print("a:", a, "b:", b)
    fibonacci.append(b)
print("Fibonacci Sonuç=",fibonacci)