import os
import sys
import time
import math
import pprint
import copy
import itertools as it
import operator as op
import bisect as bs
import functools as fn
from collections import deque, defaultdict, OrderedDict, Counter, ChainMap
maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r): return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x): return (n + x - 1) // x


osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps(): return map(int, input().split())

#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!


def better(a,b,c,N):
    ok = True   
    k =0 
    for i in range(n):
        if (a[i]+b[i])%n == c[i] and ok:
            continue
        elif (a[i]+b[i])%n < c[i]:
            k+=1
            ok = False
        else:
            break
    return k


for _ in range(*maps()):
    n, = maps()
    A = list(maps())
    B = deque(maps())
    b = list(B)
    C = [(A[i]+B[i])%n for i in range(n)]
    N = n-1
    while N:
        x = B.popleft()
        B.append(x)
        if better(A,B,C,n):
            C = [(A[i]+B[i])%n for i in range(n)]
        N-=1
    print(*C)
    