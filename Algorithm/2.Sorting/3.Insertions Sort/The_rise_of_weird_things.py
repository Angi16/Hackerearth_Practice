N=int(input())
arr = list(map(int,input().split(" ")))
a11=[]
b11=[]
for i in range(N):
	if(arr[i]%2==0):
		a11.append(arr[i])
	elif(arr[i]%2!=0):
		b11.append(arr[i])
a11.sort()
b11.sort()
for i in range(len(a11)):
	print(a11[i],end=" ")
print(sum(a11),end = " ")

for i in range(len(b11)):
	print(b11[i],end=" ")
print(sum(b11))