n=int(input())
vacst=list(map(int,input().split()))
patst=list(map(int,input().split()))
count=0
for i in range(n):
    if(vacst==patst):
        count+=1
if count==n:
    print("Yes")
else:
    print("No")