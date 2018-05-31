    INF = (1 << 30)
         
         
    def f(i, j):
        if dp[i][j] is not None:
            return dp[i][j]
        if i == j + 1:
                res = 0
        elif i == j:
            res = 1
        else:
            res = INF
            if arr[i] == arr[j]:
                res = f(i + 1, j - 1)
            else:
                for k in range(i, j):
                    res = min(res, f(i, k) + f(k + 1, j))
        dp[i][j] = res
        return dp[i][j]
        
    n = int(input())
    arr = [int(w) for w in input().split()]
    dp = [[None] * n for i in range(n)]
         
    ans = f(0, n - 1)
    print(ans)