# Taking Input From user And Store in the Binary file
# use with statement

with open('Shop.bin','wb') as f:
	n = int(input('Howmany item you want to insert : '))
	for i in range(n):
		item = input('Enter Name of Item : ')
		l = len(item)
		item = item.encode()
		f.write(item)

with open('Shop.bin','rb') as f:
	str1 = f.read()
	print(str1.decode())
