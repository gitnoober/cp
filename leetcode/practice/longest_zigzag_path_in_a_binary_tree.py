# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        N = 10**5
        [1] * N
        st = []
        ans = 0
        if root.left:
            st.append((root.left, -1, 1))
        if root.right:
            st.append((root.right, 1, 1))

        for node, side, dis in st:
            ans = max(ans, dis)
            # print(node.val, side, dis)
            if node:
                if node.left:
                    if side == 1:
                        st.append((node.left, -1, dis + 1))
                    else:
                        st.append((node.left, -1, 1))

                if node.right:
                    if side == -1:
                        st.append((node.right, 1, dis + 1))
                    else:
                        st.append((node.right, 1, 1))
        return ans
