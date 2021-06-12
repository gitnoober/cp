import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())
for _ in range(int(input())):
	a , b ,c ,d = maps()
	f=[max(a, b),max(c, d)]
	q =sorted([a,b,c,d])
	f1 ,f2 = q[-1],q[-2]
	if sorted(f) == sorted([f1,f2]):
		print('YES')
	else:
		print('NO')
