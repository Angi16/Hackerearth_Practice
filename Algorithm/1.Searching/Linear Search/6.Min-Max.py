n=int(input())
arr=list(map(int,input().split()))
maxsum=sum(arr)-max(arr)
minsum=sum(arr)-min(arr)
print(maxsum,minsum)