class Solution:
    @staticmethod
    def check(avg, weights, ans_days):
        days = 0
        summ = 0
        lst = False
        for i in weights:
            if i + summ > avg:
                summ = i
                if summ > avg:
                    return False
                days += 1
                lst = False
            else:
                summ += i
                lst = True
            print(summ, "summ", days, lst)

        if lst:
            days += 1
        print(days, ans_days, summ)
        return days == ans_days

    def shipWithinDays(self, weights, days: int) -> int:
        l = max(weights)
        h = sum(weights)
        while l < h:
            m, need, summ = (l + h) // 2, 1, 0
            for w in weights:
                if summ + w > m:
                    need += 1
                    summ = 0
                summ += w
            if need > days:
                l = m + 1
            else:
                h = m
        # print(l, h)
        return l


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
# weights = [1, 2, 3, 1, 1]
# days = 4
obj = Solution().shipWithinDays(weights, days)
print(obj)
