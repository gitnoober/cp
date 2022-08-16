
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        INF = float('inf')


        # Memoize method

        # dp = {}

        # def recur(idx, min_price):
        #   if idx >= n :
        #       return 0

        #   if (idx, min_price) in dp:
        #       return dp[(idx, min_price)]

        #   min_price = min(min_price, prices[idx])
        #   profit = prices[idx] - min_price
        #   dp[(idx, min_price)] = max(recur(idx+1, min_price), recur(idx+1, INF) + profit)
        #   return dp[(idx, min_price)]

        # x = recur(0, INF)
        # return x


        
        i = profit = 0
        buy= prices[0]
        sell = 0
        while i < n-1:
            while i < n - 1 and prices[i+1] <= prices[i]:
                i+=1
                buy = prices[i]

            while i < n - 1 and prices[i+1] > prices[i]:
                i+=1
                sell = prices[i]

            
            # print(buy, sell,sell - buy, i)
            profit += max(0, sell - buy)
            sell = buy = 0

        # print(profit)
        return max(0, profit)





prices = [3,3]
obj = Solution().maxProfit(prices)
print(obj)
