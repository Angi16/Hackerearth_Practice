def bsr(l,low,k):
	high=len(l)-1
	while(low<=high):
		mid=(low+high)//2
		if l[mid]==k:
			return mid
		elif l[mid]<k:
			low=mid+1
		else:
			high=mid-1
	return high
 
t=int(input())
for x in range(0,t):
	n,k,p=tuple(map(int,input().split()))
	l=list(map(int,input().split()))
	if n-k>=p:
		i=bsr(l,0,p)+1;ext=1
		while(ext!=0):
			ext=bsr(l,i,i+p)-i+1
			i=i+ext
		i=i+p
		if i<=n:
			print(i)
		else:
			print(-1)
	else:
		print(-1)