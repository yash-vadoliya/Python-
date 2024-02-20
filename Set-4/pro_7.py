# 07 Accept the string from user;display the count of vowels and consonants.

str = str.lower(input('Enter A string : '))
len = len(str)
vowel = 0
con = 0
spe = 0

for i in range(len):
    if(str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
        vowel += 1
    elif(str[i] == ' '):
        spe += 1
    else:
        con += 1

print('In a string Total of Vowels :',vowel)
print('In a string Total of Spaces :',spe)
print('In a string Total of Consonants :',con)
