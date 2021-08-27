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
nCr = lambda n, r :fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)

ceil = lambda a, b : (a+b-1)//b

lcm = lambda a, b: a * b // mt.gcd(a, b)

gcdm = lambda *args: reduce(mt.gcd, args, 0)

lcm = lambda a, b: a * b // mt.gcd(a, b)

lcmm = lambda *args: reduce(lcm, args, 1)


osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps(): return map(int, input().split())

#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!

n , x0 , y0 = maps()
dic = {}
for _ in range(n):
	X , Y = maps()
	if y0 - Y==0:
		dic['-1']=1
	else:
		dic[(X-x0)/(Y-y0)]=1
print(len(dic.keys()))

"""
the number of slopes would have sufficed , first solution would have been right but i forgot that the slope 
is to be calculated with respect to the gun not stupidly calculating with other points.
"""