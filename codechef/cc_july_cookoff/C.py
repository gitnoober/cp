import os
import sys
import time
import math
import pprint
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

# THINK ABOUT THE EDGE CASES ..........


for _ in range(*maps()):
	n = [*maps()][0]
	a = [*maps()]
	d = defaultdict(lambda : 0)
	for i in a:
		d[i]+=1
	ans = len(d)
	if ans == n:
		print(ans)
		continue
	arr = sorted(d.items() , key = lambda x:x[0])
	ans = min(arr[0][0]-1 , arr[0][1])
	for i in range(1,len(arr)):
		ans += min(arr[i][0]-1 ,arr[i][1])
	print(ans)



