# 17. Take two integer values from the user using split(), perform basic arithmetic operation on the values.

value = input("Enter two integer values separated by space: ")
values = value.split()

num1 = int(values[0])
num2 = int(values[1])

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

   
print(f"Sum: {add}")
print(f"Difference: {sub}")
print(f"Product: {mul}")
print(f"Quotient: {div}")


