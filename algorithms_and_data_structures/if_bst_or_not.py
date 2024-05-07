"""
Check if a tree is a BST or not

Different Approaches:
1. Check the minimum value of the right subtree of a node and the maximum value of the left subtree of a node,
and if the min value if greater than root node and the max value is less than the root node then the tree is a BST.
Not optimal.

2. Check the ranges of a tree.
O(n)

3. Do an inorder traversal and if the previous node is greater than the current node then the tree is not a BST.
O(n) and reduces the auxillary space complexity
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Approach 1
minv = [float("inf")]
maxv = [0]


def minVal(node):
    if node is None:
        return True
    minv[0] = min(minv[0], node.data)
    minVal(node.left)
    minVal(node.right)
    val = minv[0]
    minv[0] = float("inf")
    return val


def maxVal(node):
    if node is None:
        return True
    maxv[0] = max(maxv[0], node.data)
    maxVal(node.left)
    maxVal(node.right)
    val = maxv[0]
    maxv[0] = 0
    return val


def bfsutil(root):
    if root is None:
        return True

    if root.left and maxVal(root.left) >= root.data:
        return False

    if root.right and minVal(root.right) <= root.data:
        return False

    if not bfsutil(root.left) or not bfsutil(root.right):
        return False

    return True


# Approach 2
max_v = float("inf")
min_v = -float("inf")


def bfsutil(root, max_v, min_v):
    if root is None:
        return True

    if root.data < min_v or root.data > max_v:
        return False

    return bfsutil(root.left, root.data - 1, min_v) and bfsutil(
        root.right, max_v, root.data + 1
    )


# Approach 3

global prev


def is_bst(root):
    global prev
    prev = None
    return bfsutil(root)


def bfsutil(root):
    global prev
    if root is None:
        return True

    if bfsutil(root.left) is False:
        return False

    if prev is not None and prev.data > root.data:
        return False

    prev = root
    return bfsutil(root.right)


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(1)
    root.right.right = Node(4)

    # root = Node(4)
    # root.left = Node(2)
    # root.right = Node(5)
    # root.left.left = Node(1)
    # root.left.right = Node(3)
    print(is_bst(root))
