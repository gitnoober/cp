# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root):
        dic = defaultdict(list)
        # st = [root]  # node

        def dfs(root, par):
            if root:
                # dic[par.val].append(root.val)

                dfs(root.left, root)
                dfs(root.right, root)

                dic[par.val].append(root.val)


obj = Solution().findDuplicateSubtrees()
