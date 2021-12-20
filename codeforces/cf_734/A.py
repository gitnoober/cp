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
def solve1():
	Y = n//3
	if Y + 2*Y == n:
		print(Y,Y)
	else:
		if n > Y+2*Y:
			diff = n - (Y + 2*Y) ; x,y = Y,Y
			while diff:
				if diff >= 3:
					y+=1 ; x+=2 ; diff-=3
				elif diff == 2:
					y+=1 ; diff-=2
				else:
					x+=1 ; diff-=1
		else:
			diff = (Y + 2*Y) - n ; x,y = Y,Y
			while diff:
				if diff >= 3:
					y-=1 ; x-=1 ;diff-=3
				elif diff == 2:
					y-=1 ;	diff-=2
				else:
					x-=1 ;diff-=1
		print(x,y)

for _ in range(int(input())):
	a = int(input())
	c1 = a//3 +(1 if a%3 ==1 else 0)
	print(c1 , (a-c1)//2)