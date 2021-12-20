import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())
def I():return int(input())
def S():return input().rstrip('\n')
x,arr ='abcdefghijklmnopqrstuvwxyz',[]
for i in x:
	arr.append(i)
	for j in x:
		arr.append(i+j)
		for k in x:arr.append(i+j+k)
arr.sort(key = lambda x : len(x))
for _ in range(I()):
	n=I();s=S();d=c.defaultdict(int)
	for i in range(n):
		d[s[i]]+=1
		if i -1>0:
			d[s[i-1]+s[i]]+=1
		if i -1>0 and i+1<n:
			d[s[i-1]+s[i]+s[i+1]]+=1
		if i+1<n:
			d[s[i]+s[i+1]]+=1
	for i in arr:
		if not d[i]:print(i);break


