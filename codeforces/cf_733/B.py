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
def ok(i,j, arr):
	t = [(-1,0) , (0 ,-1) , (1 , 0) , (0, 1 ) , (-1 ,-1) , (-1 ,1) , (1 , -1 ) , (1 ,1)]
	for ii , jj in t:
		x ,y = i+ii , j+jj
		if x >=0 and y>=0 and x <n and y < m:
			if arr[x][y] =='1':
				return False
	return True
for _ in range(int(input())):
	n , m = maps()
	arr = [['0' for _ in range(m)] for _ in range(n)]
	for i in range(0,n,2):
		if ok(i, 0, arr):
			arr[i][0] ='1'
		if ok(i, m-1, arr):
			arr[i][m-1] ='1'
	for j in range(0,m,2):
		if ok(0,j,arr):
			arr[0][j] ='1'
		if ok(n-1, j, arr):
			arr[n-1][j] ='1'
	for i in arr:
		print(''.join(i))