# 05 Accept one integer value from the user;pdisplay appropriate day of week.

week = int(input('Enter Number of Day between 1 and 7 :'))
if(week < 7):
    if(week == 1):
        print('Sunday...')
    if(week == 2):
        print('Monday...')
    if(week == 3):
        print('Tuesday...')
    if(week == 4):
        print('Wednesday...')
    if(week == 5):
        print('Thursday...')
    if(week == 6):
        print('Friday...')
    if(week == 7):
        print('Saturday...')
else:
    print('please select a number between 1 and 7..')

