    n = int(input())
    degrees = [int(i) for i in input().split()]
    if(2 * (n - 1) == sum(degrees)):
        print('Yes')
    else:
        print('No')