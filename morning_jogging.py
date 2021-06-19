
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
	N,M = maps()
	A,ans,vis=[],[[0 for _ in range(M)] for _ in range(N)],{i : [j for j in range(M)] for i in range(N)}
	for _ in range(N):
		[A.append((_ ,i)) for i in list(maps())]
	A.sort(key=lambda x : x[1] );k=0
	while M:
		x=A[0]
		vis[x[0]].remove(k);ans[x[0]][k]=x[1]
		M-=1;k+=1;A.pop(0)
	for row , i in A:
		ans[row][vis[row].pop(0)]=i
	[print(*i) for i in ans]
	