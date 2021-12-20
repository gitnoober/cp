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
def recur(s, ans,st):
	for i in range(st , len(s)):
		if s[i] == '?':
			x = s[:i] + '1' + s[i+1:] ; y = s[:i] + '0' + s[i+1:]
			if '?' not in x:
				ans.append(x) ; ans.append(y)
			recur(x, ans, i+1) ; recur(y, ans, i+1)
	return ans
def calc(x):
	g1 , g2 = 0 , 0
	rem1 , rem2 = 5 , 5
	for i in range(10):
		if i % 2 == 0:
			g1+=int(x[i]) ; rem1-=1
		else:
			g2+=int(x[i]) ; rem2-=1
		if (g2 -g1) > rem1:return i+1
		elif (g1 - g2) > rem2:return i +1
	return 10

for _ in range(*maps()):
	s,A,ans = input().rstrip('\n'),[],10
	if '?' not in s:A.append(s)
	recur(s, A, 0)
	for i in A:ans = min(ans ,calc(i))
	print(ans)