import os
import sys
import time
import math as mt
import itertools as it
import operator as op
import bisect as bs
import heapq as hp
import functools as fn
from collections import deque, defaultdict , OrderedDict, Counter, ChainMap , _chain
maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r): return fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)


def ceil(n, x): return (n + x - 1) // x


def lcm(x , y): return x * y // mt.gcd(x,y)


osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps(): return map(int, input().split())

#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!

def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs
 
 
def modnCr(n,r):
    return fac[n] * inv[n-r] * inv[r] % mod

fac , inv = modfac(200000 , mod)

for _ in range(*maps()):
    n , k = maps()
    if n % 2 :
        cnt = 1
        for i in range(0 , n , 2):
            cnt += modnCr(n,i)
            # cnt += nCr(n,i) #number of ways to choose even number of 1's over all elements of the array
        print(pow(cnt,k,mod)) #all the choices are applied to each bit (there are total K bits)
    else:
        Pn = pow(2, n ,mod)
        cnt = 0
        for i in range(0 , n , 2):
            cnt+= modnCr(n,i) # 0 to n - 2
        cnt%=mod
        ans = pow(cnt , k , mod) #for when there are no cases when all the kth bit of n elements are set
        for i in range(k):
            ans += pow(cnt , i , mod)*1*pow(Pn , k - i - 1 , mod) #1 -- case where kth bit of all a_i's are set
            """
            leftmost part is all the ways to get & = ^ and then applying to till ith bit and i+1 bit is throughtout n number of elements is 1 and the choosing of bits of the rightmost part of kbits is of no concern because & > ^ regardless of the choice.

            """
        print(ans%mod)