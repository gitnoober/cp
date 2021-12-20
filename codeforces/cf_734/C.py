import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = 1<<60, 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())

#THINK ABOUT THE EDGE CASES ..........

def solve1(n,k,a):
	if k == n :
		[print(i,end=' ') for i in range(1 , n+1)] ;print();return 
	A = [set() for _ in range(k)]
	d = collections.defaultdict(list)
	freq = collections.defaultdict(int)
	for i in range(n):
		d[a[i]].append(i)
		freq[a[i]]+=1
	K = k
	while K:
		K-=1
		for i in freq:
			if freq[i] and i not in A[K]:
				A[K].add(i) ; freq[i]-=1
	L = [len(i) for i in A] ; avg = sum(L)//k
	# print(A,L)
	for i in range(k):
		ok = True
		idx = i
		while ok and L[i] < avg and idx < k:
			if L[idx] <= avg:
				idx+=1
			else:
				x = A[i].symmetric_difference(A[idx])
				for j in x:
					if j not in A[i]:
						A[i].add(j)
						A[idx].remove(j)
						L[i]+=1 ; L[idx]-=1
						break
	goal = min(len(i) for i in A)
	ans = [0]*n
	for i in range(k):
		Q = list(A[i])
		for j in range(goal):
			ans[d[Q[j]].pop()]=i+1
	print(*ans)
def solve2(n,k,a):
	C = [[] for _ in range(n+1)] ; s =0
	for i in range(n):
		if len(C[a[i]]) < k:
			C[a[i]].append(i) ; s +=1
	avg = s//k ; tot ,ans,cnt,ok = avg*k , [0]*n,0,True
	for i in C:
		for j in i:
			ans[j] = (cnt%k)+1 ; cnt+=1
			if cnt == tot:ok= False;break
		if not ok:break
	print(*ans)

for _ in range(int(input())):
	n , k = maps() ; a = list(maps())
	solve2(n, k, a)