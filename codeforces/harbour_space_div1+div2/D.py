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
for _ in range(*maps()):
	s = input().rstrip('\n') ; t = input().rstrip('\n')
	i, j = len(s) -1 , len(t) - 1
	while i>-1 and j >-1:
		if s[i] == t[j]:
			i-=1 ; j-=1
		else:
			i-=2
	print('YES') if j==-1 else print('NO')