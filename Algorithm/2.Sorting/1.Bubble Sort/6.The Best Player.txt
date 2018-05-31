n,m = map(int,input().split())
s={}
for i in range(n):
    k,v=input().split()
    v=int(v)
    if v not in s:
        s[v]=[k]
    else:
        s[v].append(k)
        s[v].sort()
list1=[x for x in s.keys()]
list1.sort(reverse=True)
c=0
for i in list1:
    if len(s[i])>0:
        for j in s[i]:
            print (j)
            c=c+1
            if c == m:
                break
    if c==m:
        break
 