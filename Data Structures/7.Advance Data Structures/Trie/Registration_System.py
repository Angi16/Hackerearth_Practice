n=[str(i) for i in range(200002)]
logins=set([])
last={}
T=int(input())
for i in range(T):
	s=input()
	if not s in logins:
		logins.add(s)
		print(s)
	else:	
		i=0 if s not in last else last[s]+1
		while s+n[i] in logins:
			i+=1
		last[s]=i
		s+=n[i]
		logins.add(s)
		print(s)