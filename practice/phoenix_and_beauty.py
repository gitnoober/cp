import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = 1<<60, 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline
from functools import reduce
def maps():return map(int , input().split())

#THINK ABOUT THE EDGE CASES ..........

for _ in range(*maps()):
	n , k = maps() ; a = list(maps())
	x = set(a)
	if len(x) > k:
		print(-1)
	else:
		print(n*k) ; print(*(list(x)+[1]*(k-len(x)))*n)