# 7. Accept marks from 4 students, display which mark is highest among all.

m1 = int(input('Enter Marks For Sub1 =>'))
m2 = int(input('Enter Marks For Sub2 =>'))
m3 = int(input('Enter Marks For Sub3 =>'))
m4 = int(input('Enter Marks For Sub4 =>'))

print('Mark1 =>',m1)
print('Mark2 =>',m2)
print('Mark3 =>',m3)
print('Mark4 =>',m4)

if(m1>m2 and m1>m3 and m1>m4):
	print('Mark of Sub 1 is highest :',m1)
elif(m2>m1 and m2>m3 and m2>m4):
	print('Mark of Sub 2 is highest :',m2)
elif(m3>m1 and m3>m2 and m3>m4):
	print('Mark of Sub 3 is highest :',m3)
elif(m4>m2 and m4>m3 and m4>m1):
	print('Mark of Sub 4 is highest :',m4)
else:
	print('Enter Valid Marks...')