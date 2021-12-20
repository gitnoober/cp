inf = float('inf')
import sys
import pprint
import logging
from logging import getLogger
import array
import collections

# sys.setrecursionlimit(10 ** 9)

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps(): return [int(i) for i in input().split()]


logging.basicConfig(
    format="%(message)s",
    level=logging.WARNING,
)
logger = getLogger(__name__)
logger.setLevel(logging.INFO)


def debug(msg, *args):
    logger.info(f'{msg}={pprint.pformat(args)}')

from itertools import permutations
def A():
	se = set()
	for i in permutations(input()):
		se.add(''.join(i))
	print(len(se))
	




def B():
	n, = maps()
	inn = [0]*(n+1)
	for _ in range(n-1):
		u , v = maps()
		inn[u]+=1
		inn[v]+=1
		# debug("inn" , inn)
	for i in range(1 , n + 1):
		if inn[i] >= n - 1 :
			print("Yes")
			return
	print("No")



def C():
	n , m = maps()

	B = [[*maps()] for _ in range(n)]
	if n ==1 and m == 1 :
		print("Yes")
		return

	for j in range(m):
		for i in range(1 , n):
			if B[i][j] - B[i-1][j] != 7 :
				print('No')
				return

	for i in range(n):
		for j in range(1 , m ):
			if B[i][j] - B[i][j-1] !=  1:
				print("No")
				return

	st = (B[0][0] - 1)
	f = ((st//7)*7) + 1
	
	t = 7 if not (B[0][-1] %7 ) else B[0][-1]%7
	if t != (B[0][-1] - f)+1:
		print("No")
		return

	print("Yes")




C()




