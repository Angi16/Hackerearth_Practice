from math import sqrt,ceil

T=int(input())

for _ in range(T):

	n,m=list(map(int, input().split()))

	arr=list(map(int, input().split()))

	mn=min(arr)

	mx=max(arr)

	arr.remove(mn)

	arr.remove(mx)

	mn2=min(arr)

	mx2=max(arr)

	L=4*(mx-mn)

	p=mn2-mn

	sqr=p*p*2
	
	diff=mx-mx2

	k=diff*diff*2

	res1=sqrt(diff)

	res2=sqrt(k)

	ans=L-2*p-2*diff+res1+res2

	print(ceil(ans)*m)



