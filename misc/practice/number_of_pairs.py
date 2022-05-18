
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

for _ in range(int(input())):
	n ,l, r =maps()
	a,ans =sorted(maps()),0
	for i in range(n):
		ans +=  bs.bisect_right(a, r -a[i] , lo= i+1 , hi = n) - bs.bisect_left(a, abs(a[i]- l) , lo = i+1 , hi=n)
	print(ans)
"""
[L, R] -- i+1 <= L <= n and i +1 <= R <= n
in between are the elements that could pair up with  l <= s <= r
"""
