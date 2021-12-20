import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]


for _ in range(*maps()):
	n, = maps()
	a = [*maps()]
	A = sorted(a)
	if a == A:
		print(0)
		continue
	ans = 0
	for i in range(2*n):
		if i % 2==0 :
			j = 0
			while j < n:
				if j+1 < n :
					if a[j] > a[j+1]:
						a[j] , a[j+1] = a[j+1] , a[j]
				else:
					break
				j+=2
		else:
			j = 1
			while j < n :
				if j +1 < n :
					if a[j] > a[j+1]:
						a[j] , a[j+1] = a[j+1] , a[j]
				else:
					break
				j+=2
		if a == A:
			ans = i+1
			break
	print(ans)
			