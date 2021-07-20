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
	a , b = sorted(maps())
	if a == b:
		print(0,0)
	else:
		g = b -a
		print(g , min(a%g , (g-a)%g))
#two options , reduce or increase to get the gcd g , if you reduce then it's just simple mod(distance between nearest multiple of g from a) and to increase ,
#then mod of distance between g and a 
print(os.path)