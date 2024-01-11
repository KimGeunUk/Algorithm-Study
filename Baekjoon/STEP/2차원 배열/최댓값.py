import sys
input = sys.stdin.readline

arr = []

max_num = -float('inf')
max_idx = ''
for i in range(9):
    for j, n in enumerate(list(map(int, input().split()))):
        if n > max_num:
            max_num = n
            max_idx = str(i + 1) + ' ' + str(j + 1)

print(max_num)
print(max_idx)