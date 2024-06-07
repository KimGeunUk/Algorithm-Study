import sys
input = sys.stdin.readline

N = int(input())

orders = [list(map(int, input().split())) for _ in range(N)]

count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k: continue
            
            for order in orders:
                n, s, b = order             
                x, y, z = map(int, str(n))
                
                count_s, count_b = 0, 0

                if x == i: count_s += 1
                elif (y == i or z == i): count_b += 1
                
                if y == j: count_s += 1
                elif (x == j or z == j): count_b += 1
                
                if z == k: count_s += 1
                elif (x == k or y == k): count_b += 1

                if not (s == count_s and b == count_b):
                    break
            else:
                count += 1
       
print(count)