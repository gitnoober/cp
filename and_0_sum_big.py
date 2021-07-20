# Chuck Norris played the game of thrones and won.
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())
		

n=int(input())
a=list(maps());x=list(range(1 , 2*n + 1))
a1 , a2 = a[:] ,a[:]
for i in range(2*n + 1):
	if a1 == x or a2 == x:
		print(i) ; break
	else:
		for j in range(n):
			if i % 2 == 0:
				a1[n+j],a1[j] = a1[j] ,a1[n+j]
				a2[2*j],a2[2*j +1 ] = a2[2*j +1] ,a2[2*j]
			else:
				a2[n+j],a2[j] = a2[j] ,a2[n+j]
				a1[2*j],a1[2*j +1 ] = a1[2*j +1] ,a1[2*j]
else:
	print(-1)