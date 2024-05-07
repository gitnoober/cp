class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        n = len(prices)
        # d = {}
        # def recur(idx, min_price):
        #     if idx >= n :
        #         return 0
        #     min_price = min(min_price, prices[idx])
        #     if (idx, min_price) in d :
        #         return d[(idx, min_price)]

        #     profit = prices[idx] - min_price
        #     res = max( recur(idx+1, min_price), recur(idx+1, float('inf')) + profit - fee )
        #     d[(idx, min_price)] = res
        #     return res

        # x = recur(0, float('inf'))
        # return x

        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0] - fee

        for i in range(1, n):
            buy[i] = max(
                buy[i - 1], sell[i - 1] - prices[i] - fee
            )  # keep on holding or buy some thing
            sell[i] = max(
                sell[i - 1], buy[i - 1] + prices[i]
            )  # keep on holding or sell something

        return sell[-1]


prices = [1, 3, 2, 8, 4, 9]
fee = 2
obj = Solution().maxProfit(prices, fee)
print(obj)
