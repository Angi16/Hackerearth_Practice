def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
 
T = int(input())
for _ in range(T):
    n=int(input())
    print(factorial(n))