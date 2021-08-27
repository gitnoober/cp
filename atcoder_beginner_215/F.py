import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]


def sol1():
	n, = maps()
	A = [[i for i in maps()] for _ in range(n)]
	lis_ = []

	A.sort(key= lambda x : abs(x[1] - x[0]))
	lis_.append(A[-1])
	lis_.append(A[0])

	A.sort(key= lambda x: x[0] - x[1])
	lis_.append(A[-1])
	lis_.append(A[0])

	A.sort(key= lambda x:abs(x[1] - x[0]))
	lis_.append(A[-1])
	lis_.append(A[0])

	A.sort(key= lambda x: x[0] + x[1])
	lis_.append(A[-1])
	lis_.append(A[0])

	#lis_ ---> all possible max and min values 

	ans = 0
	for i in range(len(lis_)):
		for j in range(n):
			ans = max(ans, min(abs(lis_[i][0] - A[j][0]), abs(lis_[i][1] - A[j][1])))
				
	print(ans)




def sol2():

	"""
	if you have to maximize the minimal value then most of the times binary search is the answer
	"""
	
	n, = maps()
	arr = [[*maps()] for _ in range(n)]
	arr.sort(key= lambda x: x[0])
	
	A , B = [] , []
	for i, j in arr:
		A.append(i)
		B.append(j)

	def check(x):
		#check if atleast there are two points , with distance b/w them atleast x
		j = 0
		mi , ma = 1<<60 , 0
		for i in range(n):
			while A[j] <= A[i] - x:
				mi = min(mi, B[j])
				ma = max(ma, B[j])
				j+=1
			if B[i] - mi >= x or ma - B[i] >= x:
				return True
		return False


	l , h = 0 , 10** 9
	while h - l > 1:
		m = (l+h) >> 1
		if check(m):
			l = m
		else:
			h = m
	print(l)

sol2()

