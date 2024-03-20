# Checking Wheter File Exists Or not
# We have Operating System [os] Module,it has a class named path,which has method name isfile()

import os
fname = input('Enter The Name Of File => ')
if os.path.isfile(fname):
	f = open(fname,'r')
	str1 = f.read()
	print(str1)
	f.close()
else:
	print('File Does Not Exists')
