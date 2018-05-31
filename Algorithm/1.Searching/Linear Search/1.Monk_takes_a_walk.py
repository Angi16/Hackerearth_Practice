t =input()
t=int(t)
for i in range(t):
	name=input()
	treeLetter=name.lower()
	c=0
	for chk in "aeiou":
		c+=treeLetter.count(chk)
	print(c)