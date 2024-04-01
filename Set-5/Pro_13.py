# 13. Create a function to calculate the simple interest.

def cal(amount,rate):
    print("Interest :",amount*rate/100)

amount = int(input("Enter Amount : "))
rate = int(input("Enter rate : "))
cal(amount,rate)