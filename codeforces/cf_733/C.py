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
def ok(a):
	return sum(a[-(len(a) - len(a)//4):])

for _ in range(int(input())):
	n = int(input()) ; A = sorted(maps()) ; B = sorted(maps())
	l ,r = 0 ,3*n
	ans = maxx
	while l <=  r :
		m = (l+r)//2
		a = A + [100]*m ; b = [0]*m + B
		if ok(a) >= ok(b):
			r = m -1 ; ans = min(ans, len(a))
		else:
			l = m+1
	print(ans-n)