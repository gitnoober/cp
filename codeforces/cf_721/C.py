import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr , ceil = lambda n, r: fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r) , lambda n , x: (n+x -1 )//x ; osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
input = sys.stdin.readline
def maps():return map(int , input().split())

for _ in range(int(input())):
	n = int(input()) ; a = list(maps())
	d , ans = c.defaultdict(int) , 0
	for i in range(n):
		ans+=d[a[i]]
		d[i] += i + 1
	print(ans)

	


