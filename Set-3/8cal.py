# 8. An online selling app wants to develop a application to calculate shipping charges on the
# purchase. Accept amount from the user and calculate the shipping charges.
# The shipping charges are as below:
# Shopping amount less than 1500 – The shipping charges is Rs. 100/-
# --Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/-
# --Please pay (amount+100)
# Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/-
# --Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/-
# --Please pay (amount+70)
# Shopping amount more than 3000 – Free shipping + 7% discount on amount
# --Type a message: You saved (amount*7/100)
# --Please pay (amount – discount)

amount = int(input('Enter Amount : '))

if amount<1500:
    print("Please purchase 1500 Amount to avail shipping charge of  Rs. 80/-")
    print("Please Pay :",amount," + 100 = ",amount+100)
elif amount>1500 and amount<3000:
    print("Please purchase 3000 Amount to avail shipping charge of  Rs. 50/-")
    print("Please Pay :",amount," + 70 = ",amount+70)
else:
    print("You Saved :",(amount*7/100))
    print("Please Pay :",(amount-(amount*7/100)))