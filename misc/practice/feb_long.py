from os import path
import sys
import time

# mod = int(1e9 + 7)
# import re

# from string import ascii_lowercase ,ascii_uppercase
from bisect import *

maxx = float("inf")
# ----------------------------INPUT FUNCTIONS------------------------------------------#
def I():
    return int(sys.stdin.buffer.readline())
def tup():
    return map(int, sys.stdin.buffer.readline().split())
def lint():
    return [int(x) for x in sys.stdin.buffer.readline().split()]
def S():
    return sys.stdin.readline().strip("\n")
def grid(r):
    return [lint() for i in range(r)]
def stpr(x):
    return sys.stdout.write(f"{x}" + "\n")
def star(x):
    return print(" ".join(map(str, x)))
localsys = 0
start_time = time.time()
if path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


# left shift --- num*(2**k) --(k - shift)
def s(n):
    c = 0
    arr = [True] * n
    arr[0] = arr[1] = False
    for i in range(1, int(n**0.5) + 1):
        if arr[i]:
            for j in range(2 * i, n, i):
                arr[j] = False
    cr = [0] * n
    for i in range(n):
        if arr[i]:
            c += 1
        cr[i] = c
    return cr


cnt = s(1000001)
for _ in range(I()):
    x, y = tup()
    if cnt[x] <= y:
        print("Chef")
    else:
        print("Chef")


# for _ in range(I()):
#     n = S()
#     s = S().split()
#     ht = defaultdict(set)
#     ans =0
#     for i in s:
#         ht[i[0]].add(i[1:])
#     for a ,b in combinations(ht, 2):
#         ln, lm, l  = len(ht[a]),  len(ht[b]) , len(ht[a] & ht[b])
#         ans+=(ln - l ) * (lm - l)
#     print(ans*2)


# def mulgames():
#     n , q , m = tup()
#     a = lint()
#     dp =[0]*(m+1)
#     ans =0
#     d = defaultdict(int)
#     for i in range(q):
#         l ,r = tup()
#         d[(a[l-1]+a[r-1] , a[l-1])]+=1
#     for i in d:
#         for j in range(0, m+1 , i[0]):
#             if j+i[1] <= m :dp[j+i[1]]+=d[i]
#             if j +i[0] <= m : dp[j+i[0]]-=d[i]
#     for i in range(1, m+1):
#         dp[i]+=dp[i-1]
#         ans = max(ans, dp[i])
#     print(ans)
# for _ in range(I()):
#     mulgames()


if localsys:
    print("\n\nTime Elased :", time.time() - start_time, "seconds")
