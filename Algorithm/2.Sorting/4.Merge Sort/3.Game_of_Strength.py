t = int(input())
for i in range(t):
	n = int(input())
	arr=[int(number) for number in input().split()]
	arr.sort()
	m = max(arr)
	sum1 =0
	sum2=0
	for i in range(n):
		sum1+=(arr[i]*i - sum2)
		sum2+=arr[i]
	print((sum1*m)%1000000007)