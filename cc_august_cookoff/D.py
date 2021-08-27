import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

from collections import defaultdict

def search(arr , key):
	l , h = 0 , len(arr) - 1
	idx = -1
	while l <= h :
		m = (l+h) >> 1
		if arr[m][1] >= key:
			idx = m
			l = m + 1
		else:
			h = m - 1

	return idx



for _ in range(*maps()):
	n , k , x = maps()
	A = [*maps()]
	if k == 0:
		print(sum(A))
		continue

	B = sorted([(i,j) for i , j in enumerate(A)] , key= lambda x : x[1] , reverse= True)
	i , j = 0 , 1
	ans = 0
	# print(B)
	while i < j and i < n and j < n and k > 0:
		if B[i][1] + B[j][1] > x :
			A[B[i][0]] = A[B[j][0]] = -1
			ans+=x
			k-=1
			i+=2
			j+=2
		else:
			i+=1
			j+=1
	if k == 0 :
		print(ans + sum(i if i!= -1 else 0 for i in A))
	else:

		A = [i for i in A if i != -1]
		n = len(A)
		i , j = 0 , n- 1
		while i < j :
			if A[i] + A[j] < x:
				ans+=A[i] + A[j]
				A[i] = A[j] = -1
				i+=1
				j-=1
			else:
				if k :
					ans+=x
					A[i] = A[j] = -1
					i+=1
					j-=1
				else:
					if A[i] < A[j]:
						i+=1
					else:
						j+=1
		print(ans+ sum(i for i in A if i != -1))


