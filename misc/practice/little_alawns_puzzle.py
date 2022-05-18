
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/cp/input.txt','/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())
sys.setrecursionlimit(500000)

for _ in range(int(input())):
	n = int(input()) ; a , b = list(maps()) , list(maps())
	d ,ans = {a[i]:b[i] for i in range(n)} , 0
	while d:
		ans +=1 ; k , v = d.popitem()
		while k != v:
			v = d.pop(v)
	print(pow(2 , ans , mod))