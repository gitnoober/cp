class SqrtDecomposition:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.s = int(len(arr)**0.5) + 1
        self.b = [0 for i in range(self.s)]

    def make(self):
        for i in range(self.n):
            self.b[i // self.s] += self.arr[i]

    def update(self, i, val):
        self.b[i // self.s] += val - self.arr[i]

    def query(self, l, r):
        # division operations take more time
        # i = l
        # summ = 0
        # print(self.s, self.b)
        # while i <= r:
        #     if i % self.s == 0 and i + self.s - 1 <= r:
        #         summ += self.b[i // self.s]
        #         i += self.s
        #     else:
        #         summ += self.arr[i]
        #         i += 1
        # return summ

        summ = 0
        c_l = l // self.s
        c_r = r // self.s
        if c_l == c_r:
            for i in range(l, r + 1):
                summ += self.arr[i]

        else:
            end = (c_l + 1) * self.s
            for i in range(l, end):
                summ += self.arr[i]

            for i in range(c_l + 1, c_r):
                summ += self.b[i]

            for i in range(c_r * self.s, r + 1):
                summ += self.arr[i]
        return summ
"""
Incase of the addition only , 
update - O(1)
query - O(sqrt(n))
make - O(n)

Incase of other tasks such as finding the minimum / maximum of sub-array
update - O(sqrt(n)) -- have to update the whole block , change the implementation
query - O(sqrt(n))
make - O(n)

	