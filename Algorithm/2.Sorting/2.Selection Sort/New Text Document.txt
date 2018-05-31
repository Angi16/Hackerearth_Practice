n=int(input())
frequency=[int(x) for x in input().split()]
k=int(input())
keysize=[int(x) for x in input().split()]

if n>sum(keysize):
	print('-1')
else:
	frequency.sort()
	total=0
	k=1
	while len(frequency)!=0:
		for i in range(len(keysizes)):
			try:
				total+=frequency.pop()*h
			except IndexError:
				break
			keysize[i] -= 1
		for e in keysize:
			if e==0:
				keysize.remove(e)
		k+=1
	print(total)