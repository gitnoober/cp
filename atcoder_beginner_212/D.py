import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]
import heapq
add = 0
a = []
heapq.heapify(a)
for _ in range(*maps()):
	t = input().split()
	if len(t) > 1:
		P = int(t[0])
		if P == 1:
			heapq.heappush(a , int(t[1]) - add)
		else:
			if len(a):
				add+=int(t[1])
	else:
		x = heapq.heappop(a)
		print(x+add)

	if len(a) == 0:
		add = 0
		
#add - is constant

#ughhhhhhhhhhhh how idiotic of me
