import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]



for _ in range(*maps()):
	n, = maps()
    a=int((n-1)**0.5)
    if n-a*a<=a+1:
        print(n-a*a,a+1)
    else:
        print(a+1,(a+1)**2-n+1)