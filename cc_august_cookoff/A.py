import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]
from collections import Counter
for _ in range(*maps()):
	n, = maps()
	a = [*maps()]
	if n <= 2:
		print(0)
		continue
	d = Counter(a)
	maxx = 0
	for i in d:
		maxx = max(maxx, d[i])
	if maxx == 1:
		print(n-2)
	else:
		print(n - maxx)
