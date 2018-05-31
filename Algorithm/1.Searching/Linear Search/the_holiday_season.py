from collections import defaultdict
 
n = int(input())
x = input()
d = defaultdict(int)
 
cnt = 0
 
for i in range(n-1):
    a = 0
    for j in range(i+1,n):
        if x[i] == x[j]:
            cnt += a
        a += d[x[j]]
    d[x[i]] += 1
print(cnt)