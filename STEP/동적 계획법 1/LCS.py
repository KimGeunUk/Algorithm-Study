import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

w = len(a)
h = len(b)

graph = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if b[i-1] == a[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])

print((graph.pop()).pop())

#       A  C  A  Y  K  P
#    0  0  0  0  0  0  0
# C  0  0  1  1  1  1  1
# A  0  1  1  2  2  2  2
# P  0  1  1  2  2  2  3
# C  0  1  2  2  2  2  3
# A  0  1  2  3  3  3  3
# K  0  1  2  3  3  4  4