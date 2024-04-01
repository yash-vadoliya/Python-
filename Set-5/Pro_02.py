# 2. Accept the string from the user; display the message whether the entered string is palindrome or not.

str = input('Enter String :')
if (str == str[::-1]):
    print('String is Palindrome => ',str)
else:
    print('String is not Palindrome => ',str)