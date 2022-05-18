


def solve (N, H, A, B, Q, K):
    MAXN = 300010
    # holes = [False]*200010

    # for i in H:
    #     holes[i] = True
    holes = {}
    for i in H :
        holes[i] = True

    def get_p(k):
        possible = []
        for x in range(0, MAXN):
            i = (A*x) - k
            if i >= MAXN:
                break
            if (i % B) == 0 :
                possible.append(x) # possible positions

        return possible
        # return sorted(possible)


    def bs(possible,A,B,k):
        # possible = [i for i in range(MAXN)]
        l,h= 0 , len(possible) - 1
        # possible = [i for i in range(MAXN)]
        ans = float('inf')
        while l <=h :
            m = (l+h)>>1
            y = ((A*possible[m]) - k)//B
            x = possible[m]
            dest = (A*x) - (B*y)
            if y >= 0 and dest == k:
                # print(x,y)
                if x < y + 1:
                    h = m - 1
                else:
                    ans = min(ans, x+y)
                    # print(x,y)
                    h = m - 1
            elif dest > k :
                # we need less a
                h = m - 1
            else:
                l = m + 1

        return -1 if ans == float('inf') else ans


    res = []
    for k in K:
        if k == 0 :
            res.append(k)
            continue
        if k in holes:
            res.append(-1)
            continue

        if A-B == k :
            res.append(2)
            continue

        # if k == -3:

        possible = get_p(k)
            # possible = get_p(k)
            # print(possible[:10],k,bs(possible,A,B,k))
        res.append(bs(possible,A,B,k))
        # if k == 10:
        #     print(possible[:3],k,bs(possible,A,B,k))

    return res
    # return []









    

N = int(input())
H = list(map(int, input().split()))
A = int(input())
B = int(input())
Q = int(input())
K = list(map(int, input().split()))

out_ = solve(N, H, A, B, Q, K)
print (' '.join(map(str, out_)))
# 6 2 0 16 3