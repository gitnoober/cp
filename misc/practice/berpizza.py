
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

import heapq
h=[];heapq.heapify(h)
arr=[];heapq.heapify(arr)
ans,vis,n =[],set(),1
for _ in range(int(input())):
	a =list(maps())
	if len(a) == 2:
		heapq.heappush(h, (-a[1] , n));heapq.heappush(arr, (n , a[1]))
		n+=1
	elif a[0] == 3:
		while h:
			x =heapq.heappop(h)
			if x[1] not in vis:
				ans.append(x[1]);vis.add(x[1])
				break
	elif a[0] == 2:
		while arr:
			x =heapq.heappop(arr)
			if x[0] not in vis:
				ans.append(x[0]);vis.add(x[0])
				break
print(*ans)