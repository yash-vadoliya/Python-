# MMAP : Memory Mapped File

# with open('file1.dat','wb') as f:
	# n = int(input('Howmany Records To Enter : '))
	# for i in range(n):
	# 	enr = input('Enter Enrollment Number : ')
	# 	name = input('Enter Name : ')
	# 	enr = enr.encode()
	# 	name = name.encode()
	# 	f.write(name + enr)

import mmap,sys
print('1. To View All The Data Of File')
print('2. To View Enrollment Number')
print('3. To Modify The Record')
print('4. To Exit Form File')

choice = int(input('Enter Choice Number : '))

if(choice==4):
	print('Thankyou...')
	sys.exit()
with open('file1.dat','r+b') as f:
	mm = mmap.mmap(f.fileno(),0)
	if(choice==1):
		print(mm.read().decode())
	if(choice==2):
		name = input('Enter The Name of Student To View Enrollment Number : ')
		n = mm.find(name.encode())
		n1 = n+len(name)
		enroll = mm[n1:n1+4]
		print('The Enrollment Number is => ',enroll.decode())
	if(choice==3):
		name = input('Enter The Name of Student To Modify Enrollment Number : ')
		n = mm.find(name.encode())
		n1 = n+len(name)
		new_enroll = input('Enter Enrollment Number : ')
		mm[n1:n1+4] = new_enroll.encode()
mm.close()
