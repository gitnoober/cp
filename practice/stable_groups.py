import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())


n , k , x= maps() ; a = sorted(maps())
s = sorted([(a[i] - a[i-1]) for i in range(1 , n ) if a[i] - a[i-1] > x ]) ; l = len(s) + 1
for i in s:
	p = i//x
	if  i % x ==0:
		p-=1
	if p <= k :
		k-=p;l-=1
	else:
		break
print(l)
