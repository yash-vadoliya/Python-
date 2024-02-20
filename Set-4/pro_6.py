# 06 take choice from the user ,and perform the arithmetic operation as per the choice.
# 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division

a = int(input('Enter the number of A :'))
b = int(input('Enter the number of B :'))

ch = input('Enter choice of +,-,*,/ : ')

if(ch == '+'):
    add = a + b
    print('Addition -> ',add)
elif(ch == '-'):
    sub = a - b
    print('Subtraction -> ',sub)
elif(ch == '*'):
    mul = a * b
    print('Multiplication -> ',mul)
elif(ch == '/'):
    div = a / b
    print('Division -> ',div)
else:
    print('Enter valid choice')