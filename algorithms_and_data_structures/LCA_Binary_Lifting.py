import os
import sys
import time
import math as mt


"""
O(n) solution for finding out the LCA of u and v
1.find out the path from root to u
2.find out the path from root to v
3.the last node which is common b/w both paths is the LCA
"""
class Node:
	def __init__(self ,key):
		self.key = key
		self.left = None
		self.right = None

def checkpath(root , k ,path):
	if root is None:
		return False
	path.append(root.key)
	if root.key == k:
		return True
	if checkpath(root.left , k,path) or checkpath(root.right , k , path):
		return True
	path.pop()
	return False

def LCA(root , u , v):
	path1 , path2 = [] , []
	if not checkpath(root, u , path1) or not checkpath(root , v , path2):
		return -1
	i = 0
	while i < len(path1) and i < len(path2):
		if path1[i] != path2[i]:
			break
		i+=1
	return path1[i-1]



"""
#INPUT---
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

"""

######################################__Find LCA through Binary_Lifting__##################################



"""
Finding LCA in O(logN)
Preprocessing takes O(NlogN)
1.make a table with the dp state -- dp[u][i] -- > which states the 2^ith ancestor of uth node
							y
						   /
						  /
						 /
						/
					   x
					  /
					 /
					/
				   u
dis b/w u -x -- 2^(i-1)
dis b/w x -y -- 2^(i-1)
dis b/w u - y - 2^(i-1) + 2^(i-1) = 2^i
dp[u][i] = dp[dp[u][i-1]][i-1]
2.the recurrence relation is dp[u][i] = dp[dp[u][i-1]][i-1]
3.Now, make the table and make sure you calculate the depth(height from root node) of every node using DFS
4.Now finding the LCA if level[u] < level[v] then swap these two (make sure u is deeper)
5.diff = level[u] - level[v] , (any number can be represented as a sum of power of 2's) , now if the i'th bit is set then
go up 2^ith ancestor thus reaching the 2^diff th ancestor of u 

									     LCA
									    /   \
									   /     \
									  /       \
									 /         \
									u           v
6.Now that u and v are on the same level , if the ancestor of u and v are not then change u and v to those ,(remember that ancestors beyond the dis b/w LCA and u and same for both u and v)
"""

def DFS(u,p,level,dp,L,gr):
	dp[u][0] = p
	level[u] = level[p] + 1
	for i in range(1,L+1):
		dp[u][i] = dp[dp[u][i-1]][i-1]
	for v in gr[u]:
		if v != p:
			DFS(v,u,level,dp,L,gr)

def LCA_2(level , gr , L , u ,v ):
	if level[u] < level[v]:
		u , v=  v , u
	diff = level[u] - level[v]
	for i in range(L-1 , -1 ,-1):
		if (diff << i)&1:
			u = dp[u][i]
	#now u and v are at the same level check if v is an ancestor of u
	if u == v:
		return v
	for i in range(L-1 , -1 ,-1):
		if dp[u][i] != dp[v][i]:
			u = dp[u][i]
			v = dp[v][i]
	return dp[u][0]
	
"""

# Number of nodes
n = 9
 
log = mt.ceil(mt.log(n, 2))
g = [[] for i in range(n + 1)]
 
dp = [[-1 for i in range(log + 1)] for j in range(n + 1)]

# Stores the level of each node            
level = [0 for i in range(n + 1)]
 
# Add edges
g[1].append(2)
g[2].append(1)
g[1].append(3)
g[3].append(1)
g[1].append(4)
g[4].append(1)
g[2].append(5)
g[5].append(2)
g[3].append(6)
g[6].append(3)
g[3].append(7)
g[7].append(3)
g[3].append(8)
g[8].append(3)
g[4].append(9)
g[9].append(4)
DFS(1 ,1 ,level , dp,log, g)
print(LCA_2(level , g , log , 6,8))

"""