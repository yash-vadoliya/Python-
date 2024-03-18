# Genrators

def g1(a,b):
	while a <= b:
		yield a
		a = a + 1
gen = g1(1,100)
for i in gen:
	print(i,end='')