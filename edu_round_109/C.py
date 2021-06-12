import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr , ceil = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r) , lambda n , x: (n+x -1 )//x ; osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
from fractions import Fraction
input = sys.stdin.readline
def maps():return map(int , input().split())
def solve(arr , m , ans):
	st = [] ; arr.sort()
	for x , dir , idx in arr:
		if dir == 'L':
			if not st:
				st.append((idx , -x))
			else:
				i2 , x2 = st.pop()
				ans[idx] = ans[i2] = (x - x2)//2
		else:
			st.append((idx , x))
	while len(st) >= 2:
		i1 , x1 = st.pop()
		x1 = m + (m - x1)
		i2 , x2 = st.pop()
		ans[i1] = ans[i2] = (x1-x2)//2

for _ in range(int(input())):
	n , m = maps() ; info = [*zip(list(maps()) , list(input().split()))]
	I , ans  = [[ ] , [ ]] , [-1 ]*n
	for idx in range(n):
		x , dir = info[idx]
		I[x&1].append((x , dir , idx))
	solve(I[0] , m , ans) ; solve(I[1] , m , ans)
	print(*ans)

	