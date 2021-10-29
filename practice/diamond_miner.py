
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

def rel(a, b):
	return (abs(a-b) / max(1 , abs(b)))

for _ in range(int(input())):
	x , y ,ans  =[] , []  , 0
	for i in range(2*int(input())):
		u , v = maps() ; y.append(v) if not u else x.append(u)
	print(sum(((i*i) + (j*j))**0.5 for i , j in zip(sorted(x , key = abs) , sorted(y , key = abs))))

