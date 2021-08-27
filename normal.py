import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


def func():

    n, m = maps()

    if n > m + 1 or m > 2 * (n + 1):
        print(-1)

    else:

        if n == m:  # self - explanatory
            print('10' * n)

        elif n == m + 1:  # self - explanatory
            print('01' * m + '0')

        elif 2 * n + 2 == m:  # special case
            print('110' * n + '11')
        else:
            t = m - n - 1  # '110'*t -- make the m as close to n , now m = n+1 is left
            print('110' * t + '10' * (n - t) + '1')


class Seq:

    def calc(self, s):
        S = str(s)
        return s + int(max(S)) * int(min(S))

    def solve(self):
        for _ in range(*maps()):
            a, k = maps()
            k -= 1
            prev = 0
            while k and a - prev:
                k -= 1
                prev = a
                a = calc(a)
            print(a)


from _collections import defaultdict, OrderedDict

class Young:

    def solve(self):

        for _ in range(*maps()):
            n, = maps()
            a = [*maps()]
            dic = defaultdict(int)
            gr = 0
            for i in a:
                dic[i] += 1

            # print(dic,"bef")

            for i in dic:
                x = dic[i] // i
                gr += x
                dic[i] -= x * i

            # print(dic,gr)

            rem = []
            for i in dic:
                while dic[i]:
                    rem.append(i)
                    dic[i] -= 1

            rem.sort()
            # print(rem,gr)

            i = 0
            mx = 0
            dis = 0
            while i < len(rem):
                dis += 1
                mx = max(mx, rem[i])
                if mx <= dis:
                    gr += 1
                    dis = 0
                i += 1

            print(gr)


class Johnny:

    def solve(self):
        for _ in range(*maps()):
            n, = maps()
            a = [*maps()]
            diff = [0] * n
            cc = 0
            for i in range(n):
                if i + 1 != a[i]:
                    cc += 1
                    diff[i] = 1
            if cc == n:
                print(1)
            elif cc == 0:
                print(0)
            else:
                diff = ''.join(map(str, diff)).split('0')

                x = sum([1 if len(i) else 0 for i in diff])
                print(min(2, x))


def applejack():

    n, = maps()
    a = [*maps()]
    q, = maps()
    d = defaultdict(int)
    cnt1, cnt2 = 0, 0

    for i in a:
        d[i] += 1

    for i in d:
        cnt1 += d[i] // 4  # squares
        cnt2 += (d[i] % 4) // 2  # recs each parallel side

    for i in range(q):
        s, x = input().split()
        x = int(x)
        f = d[x]
        if s == '+':
            d[x] += 1
            if f % 4 == 1:
                cnt2 += 1
            elif f % 4 == 3:
                cnt1 += 1
                cnt2 -= 1

        else:
            d[x] -= 1
            if f % 4 == 0:
                cnt1 -= 1
                cnt2 += 1
            elif f % 4 == 2:
                cnt2 -= 1

        if cnt1 > 1 or (cnt1 and cnt2 > 1):
            print('YES')
        else:
            print('NO')

    # An alternative solution is using heaps


def perform_the_combo():
    for _ in range(*maps()):
        n, m = maps()
        s = input()
        p = [*maps()]

        arr = []
        temp = [0] * 26

        for i in range(n):
            temp[ord(s[i]) - 97] += 1
            temp1 = temp[:]
            arr.append(temp1)

        ans = arr[-1]

        for i in range(m):
            for j in range(26):
                ans[j] += arr[p[i] - 1][j]

        print(*ans)
    # another way to it is by sorting the array p and counting how many times it will occur in ans


def perm_partitions():
    n, k = maps()
    a = [(i, j) for i, j in enumerate(maps())]
    a.sort(key=lambda x: x[1], reverse=True)
    pos = []
    mod = 998244353
    p = 0
    for i in range(k):
        pos.append(a[i][0])
        p += a[i][1]
    pos.sort()
    ans = 1
    for i in range(k - 1):
        ans *= pos[i + 1] - pos[i]
        ans %= mod
        # print(pos[i+1] - pos[i])
    print(p, ans)


def find(x, par):
    if x == par[x]:
        return x
    par[x] = find(par[x], par)
    return par[x]


def union(x, y, par):
    x, y = find(x, par), find(y, par)
    if x != y:
        par[x] = y


def languages():

    n, m = maps()
    l = [set([*maps()][1:]) for i in range(n)]
    if all(not len(i) for i in l):
        print(n)
        return

    par = list(range(n))

    for i in range(n):
        for j in l[i]:
            for k in range(n):
                if j in l[k]:
                    union(i, k, par)

    print(len(set(find(x, par) for x in par)) - 1)


from math import sqrt, ceil


def search(arr, key):
    l, h = 0, len(arr) - 1
    idx = -1
    while l <= h:
        m = (l + h) >> 1

        if arr[m] <= key:
            idx = m
            l = m + 1
        else:
            h = m - 1

    return idx


def pytriples():

    sq = []
    for i in range(3, 32000, 2):
        x = i * i
        y = sqrt(x)

        if y == i:
            sq.append(i * i)

        if x > 10**9:
            break
    prev = None
    ch = [0] * (10**9)
    for _ in range(*maps()):
        n, = maps()
        ans = 0

        K = sqrt(n)
        I = K
        mi = (I * I) + (I * I)

        for k in range(search(sq, mi) + 1):
            p = sq[k]
            a = ceil(p / 2)
            b = p // 2
            i = int(sqrt(p))

            if b > n:
                break

            if a != b and a <= n and b <= n and i <= n:
                ans += 1
            # ch

        if prev == None:
            prev = ans
        if prev != ans:
            print(_, prev, ans)
        prev = ans


pytriples()
