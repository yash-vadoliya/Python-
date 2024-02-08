# 7. Accept one integer value from the user; convert it to binary, octal and hexadecimal.

deci = int(input("Enter Value:"))
binary = bin(deci)
octal = oct(deci)
hexa = hex(deci)
print("Decimal : ",deci)
print("Bianry =>",binary)
print("Octal =>",octal)
print("HexaDecimal =>",hexa)