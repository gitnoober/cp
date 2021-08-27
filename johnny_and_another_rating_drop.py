import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

 

class Johnny:

    def diff(self , s1 , s2):
        if len(s1) < len(s2):
            s1 = '0'*(len(s2)-len(s1)) + s1
        return sum( i!=j for i , j in zip(s1,s2))

    def calc(self ,n):
        s1 = bin(0)[2:]
        ans = 0
        for i in range(1 , n+1):
            s2 = bin(i)[2:]
            ans+=self.diff(s1, s2)
            # print(ans,self.diff(s1, s2),i)
            s1 = s2
        return ans


    def solve(self):
        L = [0]*60
        L[0] = 1
        for i in range(1,60):
            L[i] = 2*L[i-1] + 1

        for _ in range(*maps()):
            n, = maps()
            ans = 0
            for k in range(61):
                if n & 1<<k:
                    ans+=L[k]
            print(ans)



ob = Johnny()
ob.solve()

