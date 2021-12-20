import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]
import bisect as bs



n ,  m = maps()
a = [*maps()]
b = [*maps()]

a.sort()
b.sort()

ans = 1 << 60
for i in range(n):
	idx1 = max(0 ,bs.bisect_right(b, a[i]) -1 )
	idx2 = bs.bisect_left(b, a[i])
	if idx2 == m:
		idx2-=1
	ans = min(ans, abs(a[i] - b[idx1]) , abs(a[i] - b[idx2]))


# for i in range(m):
# 	idx1 = max(0 ,bs.bisect_right(a, b[i]) -1 )
# 	idx2 = bs.bisect_left(a, b[i])
# 	if idx2 == n:
# 		idx2-=1
# 	ans = min(ans, abs(b[i] - a[idx1]) , abs(b[i] - a[idx2]))

print(ans)


