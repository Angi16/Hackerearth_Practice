from bisect import bisect_left
from itertools import accumulate
n = int(input())
sum = tuple(accumulate(map(int, input().split())))
max = sum[-1]
print(*(-1 if x > max else bisect_left(sum, x) + 1 for x in map(int, (input() for i in range(int(input()))))), sep="\n")