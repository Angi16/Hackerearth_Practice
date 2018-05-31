for _ in range(int(input())):
	n,l = map(int,input().split())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split())))
	a.sort()
	for i in range(n):
		r = a[i][0]+l
		c = a[i][1]
		for j in range(i+1,n):
			if a[j][0] <= c and a[j][1] <= r:
				c = max(c,a[j][1])
		if c == r:
			print('Yes')
			break
	else:
			print('No')