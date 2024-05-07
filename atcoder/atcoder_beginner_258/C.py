N, Q = map(int, input().split())
s = input()
curr = 0
for q in range(Q):
    t, x = map(int, input().split())
    if t == 2:
        x -= 1
        if x < curr:
            print(s[N + x - curr])
        else:
            print(s[x - curr])
    else:
        curr += x
    curr %= N


"""
all the last curr elements are in the front
that means
"""
