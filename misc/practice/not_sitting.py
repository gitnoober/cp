import sys
input = lambda : sys.stdin.readline().rstrip("\r\n")
from collections import defaultdict
from math import ceil

for _ in range(int(input())):
	n,m = map(int , input().split())
	dx = [(0,-1), (-1 , 0) , (1 , 0), (0, 1)]
	c = [(1 , 1) , (1, m) , (n,1) , (n,m)]
	a = []
	for x1 in range(1 , n+1):
		for y1 in range(1 , m+1):
			a.append(max(abs(x2-x1) + abs(y2-y1) for x2,y2 in c))
	print(*sorted(a)[:n*m])


