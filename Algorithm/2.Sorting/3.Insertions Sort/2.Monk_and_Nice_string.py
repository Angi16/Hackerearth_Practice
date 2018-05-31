n = int(input())
arr = []
for i in range(n):
	arr.append(input())
	res = 0
	for j in arr:
		if j < arr[i]:
			res += 1
	print(res)        