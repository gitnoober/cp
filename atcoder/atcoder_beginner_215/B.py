import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]


from math import log2
n, = maps()
ans = 0
for k in range(70):
	if 1 << k <= n:
		ans = k
print(ans)
