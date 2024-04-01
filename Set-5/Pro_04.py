# 4. Accept the string from the user; allow user to choose from the following options and perform the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii). Convert to the swap case, iv). Convert to the title case

str = input('Enter String : ')

print('1. Convert to the upper case ')
print('2. Convert to the lower case ')
print('3. Convert to the swap case ')
print('4. convert to the title case')

choic = int(input('Enter Your choice between 1 to 4 : '))

if(choic == 1):
    upper = str.upper()
    print('String in Upper Case => '+upper)

if(choic == 2):
    lower = str.lower()
    print('String in Lower Case => '+lower)

if(choic == 3):
    swap = str.swapcase()
    print('String in Swap Case => '+swap)

if(choic == 4):
    title = str.title()
    print('String in Title Case => '+title)
