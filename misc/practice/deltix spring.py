import os , sys,time, collections as c , math , pprint as p , itertools as it , operator as op , bisect as bs ,functools as fn
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n , x: (n+x -1 )//x 
osi, oso = '/home/priyanshu/Documents/sublimetextproject/input.txt','/home/priyanshu/Documents/sublimetextproject/output.txt'
if os.path.exists(osi):
    sys.stdin  = open(osi, 'r') ; sys.stdout = open(oso, 'w')
    
input = sys.stdin.readline

def maps():return map(int , input().split())

def A():
    for _ in range(int(input())):
        n , m = maps()
        s = list(input().rstrip('\n'))
        yes =[None]*n
        if m >= n:
            m = (m %n)+n
        while m:
            for i in range(n):
                if s[i] == '0':
                    cnt =0
                    if i > 0 and s[i-1] =='1':
                        cnt+=1
                    if i <n-1 and s[i+1] =='1':
                        cnt+=1
                    if cnt ==1:
                        yes[i]=True
            for i in range(n):
                if yes[i]==True:
                    yes[i]=False;s[i]='1'
            m-=1
        print(''.join(s))


def B():
    for _ in range(int(input())):
        n = int(input()) ; a = list(maps())
        ans,i,j =[],0,n-1
        while i < j:
            ans.append(('1',i+1,j+1))
            ans.append(('2',i+1,j+1))
            ans.append(('2',i+1,j+1))
            ans.append(('1',i+1,j+1))
            ans.append(('2',i+1,j+1))
            ans.append(('2',i+1,j+1))
            i+=1 ; j-=1
        print(len(ans))
        for i in ans:
            print(*i)


def C():
    for _ in range(int(input())):
        s =[]
        for _ in range(int(input())):
            x = int(input())
            if x == 1:
                s.append(x)
            else:
                while s and s[-1] != x-1: #keep deleting from the right till you find s[-1] ==x-1 or not s
                    s.pop()
                s[-1] = x
            print('.'.join(map(str , s)))
C()