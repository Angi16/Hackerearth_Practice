for i in range(int(raw_input())):
    n=int(raw_input())
    p=5
    sumf=1
    while sumf<=n:
        p=p*5
        sumf=(sumf*5)+1
    minp=0
    while n>0:
        p=p//5 
        sumf=sumf//5 
        q=n/sumf
        n=n%sumf
        minp=minp+q*p
    print minp