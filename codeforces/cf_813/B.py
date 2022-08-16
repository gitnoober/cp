from math import gcd
from itertools import permutations


def calc(a):
    s = 0
    n = len(a)
    for i in range(1, n + 1):
        s += (i * a[i - 1]) // gcd(i, a[i - 1])
        # print((i * a[i - 1]) // gcd(i, a[i - 1]), "ppp")
    return s


def brute(n):
    a = list(range(1, n + 1))
    ans = 0
    arr = None
    for i in permutations(a):
        x = calc(i)
        if x > ans:
            ans = x
            arr = i[:]
    return ans, arr


# ans, arr = brute(5)
# print(arr)
# (1, 3, 2, 5, 4) --- 5
# (2, 1, 4, 3, 6, 5) -- 6
# arr = (2, 1, 4, 3, 6)
# print(calc(arr))

for _ in range(int(input())):
    n = int(input())
    # if n == 1:
    #     print(1)
    #     continue
    arr = [0] * n
    # if n % 2 == 0:
    st1 = n - 2
    st2 = n - 1
    # else:
    #     st1 = n - 1
    #     st2 = n - 2
    N1 = n
    for i in range(st1, -1, -2):
        if N1 > 0:
            arr[i] = N1
            N1 -= 2
    N2 = n - 1
    for i in range(st2, -1, -2):
        if N2 > 0:
            arr[i] = N2
            N2 -= 2
    if arr[0] == 0:
        arr[0] = 1
    print(*arr)
