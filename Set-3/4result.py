# 4. A tuition class owner wants to make a simple application to allocate grade to the students on
# the basis of marks student have scored. Accept marks from the students.
# Marks more than 90 – A1 grade
# Marks 80 or less than or equal 90 – A grade
# Marks 70 or less than or equal 80 – B1
# Marks 60 or less than or equal 70 – B
# Marks 50 or less than or equal 60 – Can do Better!
# Marks <50 – Need to work hard.

a = int(input("Enter Marks :"))

if(a > 90):
	print('A1 Grade')
elif(a<90 and a>80):
	print('A Grade')
elif(a<80 and a>70):
	print('B1 Grade')
elif(a<70 and a>60):
	print('B Grade')
elif(a<60 and a>50):
	print('Can Do Better! ')
else:
	print('Need Hard Work..')
