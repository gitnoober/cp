from itertools import combinations
import sys

# n = 20
# a = list(range(n))
# for i in range(1,n+1):
# 	for j in combinations(a,i):
# 		# print(j)
# 		pass


n = int(input())
dis, direction = input().split()
a = list(map(int, input().split()))
dis = int(dis)
ok = False
for i in range(1,n+1):
	for j in combinations(a,i):
		if sum(j) == dis:
			ok = True
			break
	if ok :
		break

sys.stdout.write('Possible' if ok else 'Not Possible')
"""
5
5 Right
2 3 4 6 5
"""