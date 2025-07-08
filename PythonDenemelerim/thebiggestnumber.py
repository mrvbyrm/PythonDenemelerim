print("Finding The Biggest Number")

n1 = int(input("1. number:"))
n2 = int(input("2. number:"))
n3 = int(input("3. number:"))

max_number = n1

if n2 > max_number:
    max_number = n2
if n3 > max_number:
    max_number = n3

print("The biggest number is:", max_number)
