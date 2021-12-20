import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


from collections import deque, defaultdict
from itertools import permutations


def naive():
    arr = '1' * 6 + '0' * 6
    for i in permutations(arr, 6):
        x = ''.join(i)
        d = defaultdict(int)

        for j in range(len(x) + 1):
            for k in range(j + 1, 6):
                if len(x[j:k]) >= 3:
                    d[int(x[j:k], 2)] += 1

        ok1, ok2 = False, False
        for i in d:
            for j in d:
                if i == j and d[i] > 1:
                    ok1 = True
                elif i != j and j and i % j == 0:
                    ok2 = True

        if not ok1:
            print(x, ok1, ok2)
            print(d)
            break


naive()


for _ in range(*maps()):
    n, = maps()
    s = input()
    A = deque()
    digs = []
    k = n // 2
    summ = 0
    p = k - 1
    d = defaultdict(list)
    for i in range(k):
        if s[i] == '1':
            summ += 1 << p
        p -= 1
        A.append(s[i])

    digs.append(summ)
    d[summ].append((1, k))
    ok = False
    ANS = None
    # print(summ)
    hp = 1 << k
    left = 1

    for i in range(k, n):
        left += 1
        summ <<= 1

        if s[i] == '1':
            summ += 1

        if A[0] == '1':
            summ -= hp

        A.popleft()
        A.append(s[i])
        digs.append(summ)
        d[summ].append((left, i + 1))

        if len(d[summ]) > 1:
            ok = True
            ANS = summ

    if ok:
        print(*d[ANS][0], *d[ANS][1])
    else:
