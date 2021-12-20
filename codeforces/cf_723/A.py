import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr , ceil = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r) , lambda n , x: (n+x -1 )//x ; osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
input = sys.stdin.readline
def maps():return map(int , input().split())

for _ in range(int(input())):
	n = int(input()) ; a = list(maps()) ; N = 2*n
	ans = [0]*N ; a.sort() ; t = 1
	for i in range(1 , N, 2):
		ans[i] = a[-t] ; t+=1
	t = 0 ; k = N-2
	while k > -1:
		ans[k] = a[t] ; t+=1; k-=2
	print(*ans)
