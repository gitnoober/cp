
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

for _ in range(int(input())):
	n =int(input());s=input().rstrip('\n')
	map =collections.defaultdict(int);d,k=0,0
	for i in s:
		if i=='D':
			d+=1
		else:
			k+=1
		a,b=d,k ;gc = math.gcd(a,b)
		a/=gc;b/=gc
		map[(a,b)]+=1 ;print(map[(a,b)],end=' ')
	print()



