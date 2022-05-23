


class Solution:
    def search(self, arr, key: int) -> int:
        lo, hi = 0 , len(arr) - 1

        while lo < hi:
            m = (lo + hi) >> 1
            if arr[m] > arr[hi]:
                lo = m + 1
            else:
                hi = m
        # length will shrink by 1 

        def binary(l,h,key):
            while l<=h:
                m = (l+h)>>1
                if arr[m] == key:
                    return m
                elif arr[m] < key:
                    l = m + 1
                else:
                    h = m - 1
            return -1

        # return (binary(0,lo-1,key) | binary(lo,len(arr)-1,key)) else 
        return max(binary(0,lo-1, key), binary(lo, len(arr)-1,key))




nums, target = [1], 0
obj = Solution().search(nums,target)
print(obj)


"""
find target in the rotated array
increase then decrease

0 , 1 , 2 
"""
