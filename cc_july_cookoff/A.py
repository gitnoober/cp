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
gcd = math.gcd
for _ in range(*maps()):
	x ,y = maps()
	if gcd(x,y) > 1:
		print(0)
	else:
		ans = maxx
		for X in range(5):
			for Y in range(5):
				if gcd(x+X , Y+y) > 1:
					ans = min(ans , X+Y)
		print(ans)

