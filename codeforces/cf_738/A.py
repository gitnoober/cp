import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]



for _ in range(*maps()):
	n, = maps()
	a = [*maps()]
	ans = a[0]
	for i in range(1 , n):
		ans&=a[i]
	print(ans)