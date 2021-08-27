

class DisjointSetUnion:
	def __init__(self , n):
		self.n  = n 
		self.parent = list(range(n))
		self.size = [1]*n
		self.numsets = n

	def find(self , x):
		xcopy = a
		while self.parent[x] != x:
			x = self.parent[x]
		while xcopy != x:
			xcopy , self.parent[xcopy] = self.parent[xcopy] , x
		return x

	def union(self , x , y):
		a , b = self.find(x) , self.find(y)
		if a != b:
			if self.size[a] < self.size[b]:
				a , b = b ,a

			self.size[a]+=self.size[b] # sz.a > sz.b
			self.parent[b] = a
			self.numsets -=1

	def get_size(self , x):
		return self.size[self.find(x)]

	def __len__(self , x): #number of components 
		return self.numsets

class UnionFind:
	def __init__(self , n):
		self.parent = [i for i in range(n)]
		self.n = n 

	def find(self , x):
		xcopy = x
		while self.parent[x] != x:
			x = self.parent[x]
		while x != xcopy:
			self.parent[xcopy] , xcopy = x , self.parent[xcopy]

		return x

	def union(self ,x , y):
		self.parent[self.find(x)] = self.find(y)


