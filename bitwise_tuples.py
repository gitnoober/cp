
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn,inspect
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

def bi(a ,b ,m):
	a%=m; res =1
	while b:
		if b&1:
			res=res*a%m
		a=a*a%m
		b>>=1
	return res
	
for _ in range(int(input())):
	n,m=maps()
	print(bi(bi(2,n,mod)-1 , m , mod))
