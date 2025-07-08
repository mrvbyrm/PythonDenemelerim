print("------------- 3 ile BOLUNEBILME -------------")

for i in range(1,101):
    if(i % 3 != 0):
        continue
    print("i:",i)

print("------------- 2 ile BOLUNEBILME -------------")
liste=[]
for i in range(1,101):
    if(i % 2 != 0):
        continue
    liste.append(i)
print(liste)

print("------------- 2 ile BOLUNEBILME -------------")
liste=[i for i in range(1,101) if i % 2 == 0]
print(liste)
