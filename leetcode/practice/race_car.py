from bisect import bisect_left


class Solution:
    def racecar(self, target: int) -> int:
        arr1 = []
        arr2 = []
        arr3 = []
        pr = 0
        s1 = 1
        s2 = -1
        for i in range(10):
            arr1.append(2 * s1 - 1)
            s1 *= 2
            arr2.append(s2)
            s2 *= 2
            pr += arr2[-1]
            arr3.append(pr)
        # print(arr1, bisect_left(arr1, 10))
        # print(arr3, bisect_left(arr1, 8))
        # # print(arr3)

        # cur = 0
        # ans = []
        # while cur != target:
        #     x = target - cur
        #     idx = bisect_left(arr1,x)
        #     ans += ["A"]*(idx+1)
        #     target-=arr1[idx]

        #     x = target[]
        all_ = []
        self.op = float("inf")

        def recur(till_now, target, res):
            # print(till_now, target, res)
            if till_now == target:
                if len(res) < self.op:
                    self.op = len(res)
                    all_.append(res)
                # print(till_now, target)
                # print(len(res) < self.op)
                # all_.append(res)
                return

            if till_now > target:
                # need to subtract
                x = till_now - target
                idx = bisect_left(arr1, -x)
                y = target - arr1[idx]
                # print(idx, y, x)
                recur(y, target, res + ["R"] + ["A"] * (idx + 1))
                if idx - 1 >= 0:
                    y = target - (-1 * arr1[idx - 1])
                    recur(y, target, res + ["R"] + ["A"] * (idx))
            else:
                x = target - till_now
                idx = bisect_left(arr1, x)
                recur(till_now + arr1[idx], target, res + ["A"] * (idx + 1))

        recur(0, target, [])
        # print(all_)
        return "".join(all_[0])


target = 6
obj = Solution().racecar(target)
print(obj)
