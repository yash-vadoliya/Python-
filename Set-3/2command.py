# 2. Get the marks of 5 subject at the command line and display the total of marks, and percentage.

import sys


sub1 = int(sys.argv[1])
sub2 = int(sys.argv[2])
sub3 = int(sys.argv[3])
sub4 = int(sys.argv[4])
sub5 = int(sys.argv[5])

print('Subject1 Mark',sub1)
print('Subject2 Mark',sub2)
print('Subject3 Mark',sub3)
print('Subject4 Mark',sub4)
print('Subject5 Mark',sub5)


print('________________________')

total = sub1+sub2+sub3+sub4+sub5
print('Total : ',total)

per = total / 5
print('Percentage :',per)