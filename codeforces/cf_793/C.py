from collections import defaultdict
from itertools import permutations
from math import ceil


def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum


def brute(a):
    n = len(a)
    ans = 0
    for i in permutations(a, n):
        # print(i, lis(i))
        ans = max(ans, min(lis(i), lis(i[::-1])))
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    l = 0
    for i in d:
        d[i] = min(d[i], 2)  # don't need more than 2 occurrence
        l += d[i]
    p1 = ceil(l / 2)
    # p1 = l//2
    # p2 = brute(a)

    # print(l//2)
    print(p1)
    # if p1 != p2:
    # 	print(p1,p2,a,l)
    # 	break
