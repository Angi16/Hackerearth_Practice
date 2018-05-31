from sys import stdin, stdout
 
 
verbose = 0
 
 
def get_int_array():
    return list(map(int, stdin.readline().split()))
 
 
def solve_line(grid, row, N, K):
 
    police = []
    thief = []
 
    for i, ch in enumerate(grid[row]):
        if ch == 'P':
            police.append(i)
        else:
            thief.append(i)
 
    if verbose:
        print("row = {}".format(grid[row]))
 
    count = 0
    p = 0
    t = 0
 
    while True:
 
        if verbose:
            print("  p = {}/{}".format(p, len(police)))
            print("  t = {}/{}".format(t, len(thief)))
 
        try:
            # thief is out of range
            while thief[t] < police[p] - K:
                t += 1
        except IndexError:
            # out of police or out of thieves, we're done.
            break
 
        try:
            # police is out of range
            while police[p] < thief[t] - K:
                p += 1
        except IndexError:
            # out of police or out of thieves, we're done.
            break
 
        try:
            while abs(police[p] - thief[t]) <= K:
                count += 1
                p += 1
                t += 1
        except IndexError:
            break
 
 
    return count
 
 
 
 
def solve(grid, N, K):
    summa = 0
 
    for row in range(len(grid)):
        summa += solve_line(grid, row, N, K)
 
    return summa
 
 
 
T = int(input())
 
for _ in range(T):
    try:
        (N, K) = get_int_array()
    except ValueError:
        print(0)
        continue
 
    A = []
    for _ in range(N):
        A.append(stdin.readline().split())
 
    print(solve(A, N, K))