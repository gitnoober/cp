class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Info:
    def __init__(self):
        self.lDepth = 0
        self.rDepth = 0
        self.contains = False
        self.time = -1


class Solution:
    def __init__(self):
        self.res = {}

    def get_par_data(self, root, par):
        if root:
            root.parent = par
            self.get_par_data(root.left, root)
            self.get_par_data(root.right, root)

    def findtarget(self, root, value):
        if root:
            if root.val == value:
                return root

            x = self.findtarget(root.left, value)
            y = self.findtarget(root.right, value)
            return x if x else y

    def solve(self, root, target):
        self.get_par_data(root, None)
        node = self.findtarget(root, target)
        vis = set()

        def dfs(node, time):

            if node and node.val not in vis:
                vis.add(node.val)

                if node.val not in self.res:
                    self.res[node.val] = time

                if node.left:
                    dfs(node.left, time + 1)

                if node.right:
                    dfs(node.right, time + 1)

                if node.parent:
                    dfs(node.parent, time + 1)

        dfs(node, 0)

        return self.res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(8)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(10)
    root.left.right.left.left = TreeNode(11)
    target = 11
    s = Solution()
    print(s.solve(root, target))
