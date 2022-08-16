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


N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    infected = list(map(int, input().split()))
    saves = 0
    # while infected:
    #     can_save = {}
    #     will_save = []
    #     for i in infected:
    #         if i - 1 > 0:
    #             can_save[i - 1] = 0
    #         can_save[(i + 1) % (n + 1)] = 0
    #     mx = 0
    #     prev = 0
    #     for i in can_save:
    #         x = can_save[i] - prev
    while infected:
        se = set()
        for i in infected:
            se.add(i - 1)
            se.add((i + 1) % (n + 1))
        mx = 0
        num = None
        for i in infected:
            will_be_saved = 0
            if i - 1 not in se and i - 1 > 0:
                will_be_saved += i
            if will_be_saved > mx:
                mx = will_be_saved
