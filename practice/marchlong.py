from os import path
import sys,time
# mod = int(1e9 + 7)
from math import ceil, floor,gcd,log,log2 ,factorial,sqrt
from collections import defaultdict ,Counter , OrderedDict , deque;from itertools import combinations,permutations
# from string import ascii_lowercase ,ascii_uppercase
from bisect import *;from functools import reduce;from operator import mul;maxx = float('inf')
I = lambda :int(sys.stdin.buffer.readline())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().strip('\n')
grid = lambda  r :[lint() for i in range(r)]
localsys = 0
start_time = time.time()
#left shift --- num*(2**k) --(k - shift)
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
def ceill(n,x):
    return (n+x -1 )//x
T =1

def solve():#college_ life 4
    n , e , h , a ,b ,c = lint()
    ans = maxx
    for i in range(n+1):
        if e < i or h < i :
            break
        left = n - i
        eggs = e - i
        choc = h - i
        price = i*c
        if a < b:
            k = min(left , eggs//2)
            price+=k*a
            left-=k
            if left <= choc//3:
                price+= left*b
                ans = min(ans ,price)
        else:
            k = min(left, choc//3)
            price+= k*b
            left-=k
            if left <= eggs//2:
                price+= left*a
                ans = min(ans , price)
    print(-1 if ans == maxx else ans)





                    



    





    








def run():
    if (path.exists('input.txt')):
        sys.stdin=open('input.txt','r')
        sys.stdout=open('output.txt','w')


run()
T = I() if T else 1
for _ in range(T):
    solve()


if localsys:
    print("\n\nTime Elased :",time.time() - start_time,"seconds")