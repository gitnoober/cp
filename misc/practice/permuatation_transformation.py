
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

def recur(a , level,ans ):
	if not a:
		return
	m = max(a)
	if m :
		ans[m]=level ; idx = a.index(m)
		recur(a[:idx], level+1, ans) ;recur(a[idx+1:], level+1, ans)
	else:return


for _ in range(int(input())):
	n = int(input()) ; a =list(maps()) ;ans = {}
	recur(a, 0, ans)
	print(*[ans[a[i]] for i in range(n)])
