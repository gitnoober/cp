import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]


maxx = 1<<60
def naive(s,k):
	st = 'wudiduw'
	A = 0
	cnt = 0
	for i in range(0 , n, k):
		f = s[i:i+k]
		# if cnt == 1:
		# 	cnt+=1
		# 	continue
		for j in range(k):
			if f[j] != st[j]:
				A+=1
		cnt+=1

	# print(A)




for _ in range(*maps()):
	n , k = maps()
	s = input()
	d = {i:[0]*26 for i in range(k)}

	ans = 0
	i = 0
	tot = n//k

	while i < n:
		d[i%k][ord(s[i])-97]+=1
		i+=1
	

	for i in range(k//2):
		tt = [i+j for i,j in zip(d[i] , d[k-i-1])]
		ans += 2*tot - max(tt)


	if k% 2:
		ans += tot - max(d[k//2])
	
	print(ans)


	

			

