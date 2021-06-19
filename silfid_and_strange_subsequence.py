
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

for _ in range(int(input())):
	n=int(input());a=list(maps())
	po,ne,z=[],[],0
	for i in a:
		if i==0:
			z+=1
		po.append(i) if i > 0 else ne.append(i)
	po.sort();N,ok=len(ne),True
	if po:
		ne.sort()
		for i in range(N-1):
			if abs(ne[i] - ne[i+1]) <po[0]:
				ok=False;break

	print(N if not ok else max(1, N-z + (1 if po else 0)+(1 if z else 0),N))
	