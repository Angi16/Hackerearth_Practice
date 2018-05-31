t=int(input())
for i in range(t):
	n=input()
	if('21' in n):
		print("The streak is broken!")
	elif(int(n)%21==0):
		print("The streak is broken!")
	else:
		print("The streak lives still in our heart!")