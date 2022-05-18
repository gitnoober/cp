import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr , ceil = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r) , lambda n , x: (n+x -1 )//x ; osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
input = sys.stdin.readline
def maps():return map(int , input().split())

for _ in range(int(input())):
	n = int(input()) ; a = list(maps())
	d ,s ,v , ans = c.defaultdict(int) , set() , [] , maxx
	for i in a:
		d[i]+=1
	for i in d:
		s.add(d[i]) ; v.append(d[i])
	for x in s:
		tot = 0
		for i in v:
			tot += i -x if i >= x else i
		ans = min(ans , tot)
	print(ans)
"""
iterating through only the unique elements reduces the constants and it can be proven that the C will be in the list of the occurences , 
becuase taking C not in the occ. list will not be any better , also iterating through only the unique elements reduces the constant , 
reducing the original O(n*n) to O(n*(n^.5))
"""

