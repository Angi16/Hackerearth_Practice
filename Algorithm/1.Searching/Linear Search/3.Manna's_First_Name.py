t=input()
t=int(t)
for _ in range(t):
	names=input()
	names=names.upper()
	c1=names.count("SUVO")
	c2=names.count("SUVOJIT")
	print('SUVO = '+str(c1-c2)+', SUVOJIT = '+str(c2))