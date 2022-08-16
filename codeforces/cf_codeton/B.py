class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
        self.numsets = n

    def find(self, x):
        xcopy = x
        while self.parent[x] != x:
            x = self.parent[x]
        while xcopy != x:
            xcopy, self.parent[xcopy] = self.parent[xcopy], x
        return x

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.size[a] += self.size[b]  # sz.a > sz.b
            self.parent[b] = a
            self.numsets -= 1

    def get_size(self, x):
        return self.size[self.find(x)]

    def __len__(self):  # number of components
        return self.numsets


def has_intersection(tuple_1, tuple_2):
    return max(tuple_1) >= min(tuple_2) and max(tuple_2) >= min(tuple_1)


def func1(n, x, a):
    c = 0
    mx = a[0]
    mi = a[0]
    for i in range(n):
        mx = max(mx, a[i])
        mi = min(mi, a[i])
        if mx - mi > x * 2:
            mx = a[i]
            mi = a[i]
            c += 1
    return c


def func2(n, x, a):
    tree = DisjointSetUnion(n)
    cur_mi = a[0] - x
    cur_mx = a[0] + x
    for i in range(1, n):
        l = a[i] - x
        r = a[i] + x
        if has_intersection((l, r), (cur_mi, cur_mx)):
            # print(i - 1, i, (cur_mi, cur_mx), (l, r))
            tree.union(i - 1, i)
            cur_mi = min(l, cur_mi)
            cur_mx = max(r, cur_mx)
        else:
            cur_mi = a[i] - x
            cur_mx = a[i] + x
    ans = tree.__len__() - 1
    # print(ans)
    return ans


N = int(input())
for _ in range(N):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans1 = func1(n, x, a)
    print(ans1)
    # ans2 = func2(n, x, a)
    # if ans1 != ans2:
    # print(ans1, ans2, a, x)

#     tree = DisjointSetUnion(n)
#     cur_mi = a[0] - x
#     cur_mx = a[0] + x
#     for i in range(1, n):
#         l = a[i] - x
#         r = a[i] + x
#         if has_intersection((l, r), (cur_mi, cur_mx)):
#             tree.union(i - 1, i)
#         else:
#             cur_mi = a[i] - x
#             cur_mx = a[i] + x
#     ans = tree.__len__() - 1
#     print(ans)
