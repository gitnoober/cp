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
for _ in range(int(input())):
	n = int(input()) ; a = [*maps()]
	A = sorted(a)[::2] ; B = sorted(a[::2])
	print('YES') if A == B else print('NO')
"""
can only swap at even distances ,i.e if elements at odd position before sorting and after sorting stay the 
same regardless of their disposition , it is correct, same can be said about elements at even position
"""