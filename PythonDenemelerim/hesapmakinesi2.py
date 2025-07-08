print("*****************************")
print("Calculator Program\n")
print("1-Addition Operation")
print("2-Subtraction Operation")
print("3-Multiplication Operation")
print("4-Division Operation")
print("*****************************")
while True:
    op = input("Enter Operation:")

    if op in ["1", "2", "3", "4"]:
        n1 = float(input("First number:"))
        n2 = float(input("Second number:"))

        if op == "1":
            print("op:+")
            print("Result =", (n1 + n2))
        elif op == "2":
            print("op:-")
            print("Result =", (n1 - n2))
        elif op == "3":
            print("op:x")
            print("Result =", (n1 * n2))
        elif op == "4":
            print("op:/")
            if n2 != 0:
                print("Result =", (n1 / n2))
            else:
                print("Invalid Operation! Division by zero is not allowed.")
    else:
        print("Error! Invalid Operation...")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break

print("Calculator program has ended.")