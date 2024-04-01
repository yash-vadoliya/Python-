# 14. Create a function to perform basic arithmetic operations on the number.

def cal(val1,val2):
    print("Sum of {} + {} = {}".format(val1,val2,val1+val2))
    print("Substration of {} - {} = {}".format(val1,val2,val1-val2))
    print("Multiplication of {} X {} = {}".format(val1,val2,val1*val2))
    print("Divison of {} / {} = {}".format(val1,val2,val1/val2))

a = int(input("Enter Value 1 :"))
b = int(input("Enter Value 2 :"))
print("--------------------------------------")
cal(a,b)