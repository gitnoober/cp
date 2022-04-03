class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pass


# if x or y  co-ordinate is 0 then you have reached the pacific ocean
# if x or y  co-ordinate is n-1 then you have reached the atlantic ocean


heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
obj = Solution().pacificAtlantic(heights)
print(obj)
