"""
Find path from root to n1 and root to n2
"""


class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findpath(path, src, dest):
    if src is None:
        return False

    path.append(src.key)
    if src.key == dest:
        return True

    if (src.left is not None and findpath(path, src.left, dest)) or (
        src.right is not None and findpath(path, src.right, dest)
    ):
        return True

    path.pop()
    return False


def lca(root, n1, n2):
    path1, path2 = [], []

    if not findpath(path1, root, n1) or not findpath(path2, root, n2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2) and path1[i] == path2[i]:
        i += 1
    return path1[i - 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(lca(root, 4, 5))
