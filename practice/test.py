# # Python program to for tree traversals

# # A class that represents an individual node in a
# # Binary Tree


# class Node:
# 	def __init__(self, key):
# 		self.left = None
# 		self.right = None
# 		self.val = key


# # A function to do inorder tree traversal
# def printInorder(root):

# 	if root:

# 		# First recur on left child
# 		printInorder(root.left)

# 		# then print the data of node
# 		print(root.val)

# 		# now recur on right child
# 		printInorder(root.right)


# # A function to do postorder tree traversal
# def printPostorder(root):

# 	if root:

# 		# First recur on left child
# 		printPostorder(root.left)

# 		# the recur on right child
# 		printPostorder(root.right)

# 		# now print the data of node
# 		print(root.val),


# # A function to do preorder tree traversal
# def printPreorder(root):

# 	if root:

# 		# First print the data of node
# 		print(root.val),

# 		# Then recur on left child
# 		printPreorder(root.left)

# 		# Finally recur on right child
# 		printPreorder(root.right)


# # Driver code
# root = Node(5)
# root.left = Node(3)
# # root.right = Node(3)
# root.left.left = Node(2)
# # root.left.right = Node(5)
# root.left.right = Node(4)
# root.left.right.left = Node(1)
# # print "Preorder traversal of binary tree is"
# # printPreorder(root)

# # print "\nInorder traversal of binary tree is"
# printInorder(root)

# # print "\nPostorder traversal of binary tree is"
# # printPostorder(root)

# N_ary_Tree Python program
class Node:
    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children or []
        self.parent = parent or []
        self.locked = False
        self.uid = None

    def __str__(self):
        return str(self.data)


class N_ary_Tree:
    def __init__(self):
        self.root = None

    def find_node(self, node, key):
        if node is None or node.data == key:
            return node
        for child in node.children:
            return_node = self.find_node(child, key)
            if return_node:
                return return_node
        return None

    def add(self, data, parent=None):
        new_node = Node(data)
        # print(data,"data")
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.find_node(self.root, parent)
            parent_node.children.append(new_node)
            new_node.parent = parent_node

    def lock(self, val, uid):
        node = self.find_node(self.root, val)
        parent_node = node.parent
        if node.locked == False and parent_node.locked == False:
            for child in node.children:
                if child.locked == False:
                    continue
                else:
                    return False
            node.locked = True
            node.uid = uid
            return True
        else:
            return False

    def unlock(self, val, uid):
        node = self.find_node(self.root, val)
        if node.uid == uid:
            node.locked = False
            return True
        else:
            return False

    def upgrade(self, val, uid):
        node = self.find_node(self.root, val)
        for child in node.children:
            if child.locked == True and child.uid == uid:
                continue
            else:
                return False
        node.locked = True
        node.uid = uid
        for child in node.children:
            child.locked = False
            child.uid = None
        return True

    def print_tree(self, node, str_aux):
        if node is None:
            return ""
        str_aux += str(node) + " Locked=" + str(node.locked) + \
            "UID:" + str(node.uid) + '('
        for i in range(len(node.children)):
            child = node.children[i]
            end = ',' if i < len(node.children) - 1 else ''
            str_aux = self.print_tree(child, str_aux) + end
        str_aux += ')'
        return str_aux

    def __str__(self):
        return self.print_tree(self.root, "")


# main method
# if __name__ == "__main__":
#     n = int(input())
#     m = int(input())
#     que = int(input())
#     lt = []
#     for i in range(n):
#         st = input()
#         lt.append(st)
#     tree = N_ary_Tree()
#     tree.add(lt[0])
#     i = 1
#     key = [lt[0]]
#     while i < n:
#         temp = []
#         for ele in key:
#             if i < n:
#                 for j in range(m):
#                     print(lt[i], ele, "pp", temp)
#                     tree.add(lt[i], ele)
#                     temp.append(lt[i])
#                     i += 1
#             else:
#                 break
#         key.clear()
#         key = temp
    # print(tree)

    # for i in range(que):
    #     temp = input().split()
    #     op_type = int(temp[0])
    #     node = temp[1]
    #     user_id = int(temp[2])
    #     if op_type == 1:
    #         print(tree.lock(node, user_id))
    #     elif op_type == 2:
    #         print(tree.unlock(node, user_id))
    #     elif op_type == 3:
    #         print(tree.upgrade(node, user_id))

# 'ccc' - 0


# N = 20
# gr = [[] for _ in range(N)]
# while True:
#     try:
#         u, v = map(int, input().split())
#     except:
#         break
#     gr[u].append(v)  # u - v
# # print(gr)
# dist = [0] * N
# q = [(1, 0)]  # root node , level
# vis = {1}  # already visited

# for node, dis in q:
#     for v in gr[node]:
#         if v in vis:  # O(1)
#             break
#         q.append((v, dis + 1))
#         dist[v] = dis + 1
#         vis.add(v)  # not really needed, but just in case if there are self loops
# print(dist[:20])
# from collections import defaultdict
# dic = defaultdict(int) # 2 , -1
# for node in range(len(dist)):
# 	dic[dist[node]].append(node)

# d = {1 : { 2 : {11 : ["ABC","CDE"] , 5 : { 8 : {12} , 9 : [] , 12 : []} } , 7 : {}  } }


# data = {'sub' : 1, 'sub-sub' : 1 ,'category' : 1, 'link' : 1 }
# A = [
# 	{'sub' : 1, 'sub-sub' : 1 ,'category' : 1, 'link' : 1 }
# 	---------------------------------------------------------
# 	{'sub' : 1, 'sub-sub' : 1 ,'category' : 2, 'link' : 2 },
# 	---------------------------------------------------------
# 	{'sub' : 1, 'sub-sub' : 1 ,'category' : 4, 'link' : 1 }

# 	{'sub' : 2, 'sub-sub' : 3 ,'category' : 1, 'link' : 1 }
# 	{'sub' : 2, 'sub-sub' : 3 ,'category' : 2, 'link' : 3 }
# 	{'sub' : 2, 'sub-sub' : 4 ,'category' : 1, 'link' : 1 },
# 	{'sub' : 3, 'sub-sub' : 1 ,'category' : 4, 'link' : 4 },
# 	-------------------------------------------------------
# 	{'sub' : 5, 'sub-sub' : 5 ,'category' : 1, 'link' : 2 },
# 	{'sub' : 5, 'sub-sub' : 5 ,'category' : 1, 'link' : 3 },
# ]
# d = {
# 	  'math' ,
# 	  'sst',
# }

# normal             result


# data = [sub , sub-sub , ]
# sub -  subject(SST)
# sub-sub - civics,geo
# link - []

class Node:
    def __init__(self, subject=None, klass=None, medium=None, category=None, sub_subject=None, links=[]):
        # self.data = data
        # self.children = children or []
        # self.parent = parent or []
        # self.locked = False
        # self.uid = None
        self.subject = subject
        self.klass = klass
        self.medium = medium
        self.category = category
        self.sub_subject = sub_subject
        self.links = links

    # def __str__(self):
    #     return str(self.data)
# N = 1000
# visited = [False]*N
# adj = [[] for _ in range(N)]
# def dfs(a,b):
from pprint import pprint

n = int(input())
A = []
num_params = 6
for _ in range(n):
    dic = {}
    for __ in range(num_params):
        s = input().split(':')
        dic[s[0]] = s[1]
    input()
    A.append(dic)
# pprint(A)


def make_tree(A):
    # sample inputs can be always be called in real-world as it is stored in db
    all_subject = ['math', 'chemistry']
    all_class = ['6', '7', '8', '9', '10', '11', '12']
    all_medium = ['hindi', 'english', 'bengali']
    all_category = ['ncert', 'rdsharma']
    all_sub_subject = ['civics', 'null', 'geography']
    tree = {}
    for i in all_subject:
        tree[i] = {}
        for j in all_class:
            tree[i][j] = {}
            for k in all_medium:
                tree[i][j][k] = {}
                for l in all_category:
                    tree[i][j][k][l] = {}
                    for m in all_sub_subject:
                        tree[i][j][k][l][m] = {'links': []}

    pprint(tree)


make_tree(A)
