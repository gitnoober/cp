import os,sys,time
oso = '/home/priyanshu/Documents/cp/input.txt'
if os.path.exists(oso):sys.stdout = open(oso, 'w')
import random
print(100)
for _ in range(100):
	# print(10000)
	x = random.randint(1, 100000)
	print(x)
	for i in range(x):
		print(random.randint(0, 100),end=' ')
	print()
	for i in range(x):
		print(random.randint(0, 100),end=' ')
	print()