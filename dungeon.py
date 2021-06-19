
import os , sys,time, collections , math , pprint , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
	sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
	
input = sys.stdin.readline

def maps():return map(int , input().split())


for _ in range(int(input())):
	a=list(maps());s=sum(a)
	print('YES' if min(a)>=s//9 else 'NO') if not s % 9 else print('NO')
	
"""
since every 7 moves it deals 9 damage,
so in order for all the monsters to die at 7k , a+b+c has to be divisible by 9 ,and the min (a,b,c) >= (a+b+c)/9
"""