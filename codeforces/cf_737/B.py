import os
import sys
import math as mt

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)


def nCr(n, r):
    return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x):
    return (n + x - 1) // x


def lcm(x, y):
    return x * y // mt.gcd(x, y)


osi, oso = (
    "/home/priyanshu/Documents/cp/input.txt",
    "/home/priyanshu/Documents/cp/output.txt",
)
if os.path.exists(osi):
    sys.stdin = open(osi, "r")
    sys.stdout = open(oso, "w")

input = sys.stdin.readline


def maps():
    return map(int, input().split())


#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!


def search(arr, key):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            h = m - 1
        else:
            l = m + 1
    return -1


for _ in range(*maps()):
    n, k = maps()
    a = [*maps()]
    if k == n:
        print("Yes")
        continue
    A = sorted(a)
    d = {A[i]: i for i in range(n)}
    tk = []
    i = 0
    while i < n:
        temp = [a[i]]
        idx = i + 1
        while idx < n:
            index = d[a[idx]]
            if (
                A[index - 1] == a[idx - 1]
                and A[index - 1] < A[index]
                and a[idx - 1] < a[idx]
            ):
                temp.append(a[idx])
                idx += 1
            else:
                break
        i = idx
        tk.append(temp)
    N = len(tk)
    if N > k:
        print("No")
    else:
        print("Yes")
