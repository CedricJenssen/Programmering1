#Henter første nummer fra bruker
num1 = float(input("Enter number: "))
#Velger operator som skal tas i bruk
op = input("Enter operator: ")
#Velger andre nummer fra bruker
num2 = float(input("Enter number: "))

#Hvis operator er x utfører den regnstykke i print under
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
elif op == "**":
    print(num1 ** num2)
elif op == "//":
    print(num1 // num2)