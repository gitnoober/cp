import os , sys,time, collections , math , pprint as pp, itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

for _ in range(int(input())):
	n = int(input()) ; a =[0]+ list(maps()) +[0]
	ans =0
	for i in range(n+1):
		x = min(a[i], max(a[i-1] , a[i+1]))
		ans += a[i] - x + abs(a[i-1] - x) ; a[i] = x
	print(ans+a[n])
