import collections

class Solution:
    def deleteAndEarn(self, nums) -> int:
        
        freq = collections.defaultdict(int)
        n = len(nums)
        tot_sum = 0

        for i in range(n):
            freq[nums[i]]+=1
            tot_sum += nums[i]

        arr = list(set(nums))
        N = len(arr)

        def recur(res,i):
            if i >= N :
                return 0

            val = (freq[arr[i]]*arr[i])
            r = (freq[arr[i]+1]*(arr[i]+1)) + (freq[arr[i]-1]*(arr[i]-1))

            x = max(val + recur(res-(r+val), i+1), recur(res,i+1))
            print(x, "x")
            return x

        ans = recur(tot_sum, 0)
        print(ans, "ans")






nums = [3,4,2]
obj = Solution().deleteAndEarn(nums)
print(obj)
        