# import sys

# # def input(): return sys.stdin.readline().rstrip("\r\n")

# def maps():return [int(i) for i in input().split()]

# #lOOKOUT FOR THE EDGE CASES

# for _ in range(int(input())):
# 	n = int(input())
# 	s = input()
# 	if len(set(s)) == 1 :
# 		print(n)
# 	else:
# 		if n % 2 :
# 			print(1)
# 		else:
# 			j = n//2
# 			x = s[j]
# 			print(x, s[j+1] , j+1,n)
# 			while j+1 < n and x == s[j+1]:
# 				j+=1

# 			i = n//2
# 			while i > 0 and x == s[i-1]:
# 				i-=1

# 			l = (j-1) - (i+1) + 1
# 			print(l, i ,j)


# def input(): return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# lOOKOUT FOR THE EDGE CASES

for _ in range(int(input())):
    n = int(input())
    s = input()
    if len(set(s)) == 1:
        print(n)
    else:
        # if n % 2 :
        # 	print(1)
        # else:
        j = n // 2
        x = s[j]
        while j < n and x == s[j]:
            j += 1

        i = n // 2
        while i >= 0 and x == s[i]:
            i -= 1
        l = (j - 1) - (i + 1) + 1
        print(l)
