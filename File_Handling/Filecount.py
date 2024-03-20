import os
fname = input('Enter The Name Of File => ')
if os.path.isfile(fname):
	f = open(fname,'r')
else:
	print(fname,'Does Not Exists..')

cl = cw = cc = 0
# cl = Count Line, cw = Count Word, cc = Count Charaxter
for line in f:
	word = line.split()
	cl = cl+1
	cw = cw + len(word)
	cc = cc + len(line)
print('Number Of Line in a File is : ',cl)
print('Number Of Words in a File is : ',cw)
print('Number Of Character in a File is : ',cc)
f.close()