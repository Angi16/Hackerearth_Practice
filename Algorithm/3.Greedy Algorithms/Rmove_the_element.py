    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        arr.sort()
        arr.reverse()
        c=arr[0]
        
        for j in range(1,n):
            for i in range(1,n):
                arr[i]+=arr[i]*(j)
            c+=arr[j]
        c=c%1000000007
        print(c)