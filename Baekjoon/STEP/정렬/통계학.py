# import sys
# input = sys.stdin.readline

# N = int(input())

# L = list()
# D = dict()

# for _ in range(N):
#     a = int(input())
#     L.append(a)
#     if a in D:
#         D[a] += 1
#     else:
#         D[a] = 1

# D = sorted(D.items(), key=lambda x:(-x[1], x[0]))
# L.sort()
 
# print(round(sum(L) / N))
# print(L[N//2])

# if len(L) == 1: print(D[0][0])
# elif D[1][1] == D[0][1]: print(D[1][0])
# else: print(D[0][0])

# if len(L) == 1: print(0)
# else: print(L[-1] - L[0])

import sys
input=sys.stdin.readline

from collections import Counter

N = int(input())
L = [int(input()) for _ in range(N)]

L.sort()
print(round(sum(L) / N))
print(L[N//2])

c = Counter(L).most_common()
print(c)
if len(c) > 1 and c[0][1] == c[1][1]: print(c[1][0])
else: print(c[0][0])

if len(L) == 1: print(0)
else: print(L[-1] - L[0])