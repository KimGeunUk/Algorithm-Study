import sys
input = sys.stdin.readline

K = int(input())

direct = []
nums = []
h = []
w = []

for _ in range(6):
    d, n = map(int, input().split())
    
    direct.append(d)
    nums.append(n)
    
    if d == 4 or d == 3:
        h.append(n)
    elif d == 1 or d == 2:
        w.append(n)

direct = direct*2
nums = nums*2

rect = max(h) * max(w)

for i in range(len(direct)-1):
    if direct[i:i+2] == [1, 3] or direct[i:i+2] == [4, 1] or direct[i:i+2] == [2, 4] or direct[i:i+2] == [3, 2]: 
        rect = rect - nums[i:i+2][0] * nums[i:i+2][1]
        break

print(rect*K)
        


