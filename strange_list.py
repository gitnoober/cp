
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

#think about the edge cases 
for _ in range(int(input())):
	n ,x = maps() ;a = list(maps()) ; ans = sum(a) ; b =a[:] ; ok = True
	while ok:
		for i in range(n):
			if b[i] % x ==0:
				b[i]//=x ; ans+=a[i]
			else:
				ok = False
				break
	print(ans)


