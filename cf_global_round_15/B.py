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
def better(A,B):
	cnt =0
	for idx in range(5):
		if (A[idx] < B[idx]):
			cnt+=1
	return True if cnt >=3 else False
for _ in range(*maps()):
	n = [*maps()][0] ; a = [[*maps()] for _ in range(n)]
	best = a[0] ; I = 0
	for i in range(1,n):
		if not better(best, a[i]):
			best = a[i] ; I = i
	for i in range(n):
		if i!= I and not better(best, a[i]):
			print('-1') ; break
	else:
		print(I+1)

