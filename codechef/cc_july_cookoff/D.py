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

for i in range(*maps()):
	n = [*maps()][0]
	a = [*maps()]
	a.sort()
	mi = a[0]
	ok = True
	for i in range(1,n):
		if a[i] != mi and (a[i] % (a[i]-mi)) !=mi:
			ok = False
			break
	if ok:
		print(n - a.count(mi))
	else:
		print(n)
