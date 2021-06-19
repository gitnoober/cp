import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn,heapq
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps():return map(int , input().split())

for _ in range(int(input())):
	n , q =maps()
	a =sorted(maps()) ;b=sorted(maps());queries =[int(input()) for _ in range(q)]
	h ,cur,d,vis= [(a[0]+b[0],0,0)],1,{},{(0,0):True}
	while h and cur < 10001:
		x,i,j=heapq.heappop(h)
		if i + 1 <n and (i+1,j) not in vis:
			heapq.heappush(h,(a[i+1]+b[j],i+1,j))
			vis[(i+1,j)]=1
		if j + 1 <n and (i,j+1) not in vis:
			heapq.heappush(h,(a[i]+b[j+1],i,j+1) )
			vis[(i,j+1)]=1
		d[cur]=x
		cur+=1
	[print(d[i]) for i in queries]