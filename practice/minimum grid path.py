import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr , ceil = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r) , lambda n , x: (n+x -1 )//x ; osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
input = sys.stdin.readline
def maps():return map(int , input().split())
for _ in range(int(input())):
	n =int(input()); c = list(maps())
	rem , s, mn , ans  = [n , n] , [0 ,0 ] , [maxx , maxx] , maxx
	for i in range(n):
		rem[i%2]-=1 ; s[i%2]+=c[i] ; mn[i%2] = min(c[i], mn[i%2])
		ans = min(ans , s[0] + mn[0]*rem[0]  + s[1] + mn[1]*rem[1])
	print(ans)
"""
length of the vertical path = length of the horizontal path , since it is alternating it has to odd even positions
so , min of the vertical path * rest + (one of each path) + min of the horizontal path * rest + one of each path
"""