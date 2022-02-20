from heapq import heapify, heappush, heappop
for _ in range(int(input())):
	n = int(input())
	a = list(map(int , input().split()))
	if a == sorted(a):
		print('NO')
	else:
		print('YES')