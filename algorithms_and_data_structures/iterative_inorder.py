def recur(root):
    stack = []
    ans = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        ans.append(r)
        root = root.right

    return ans
