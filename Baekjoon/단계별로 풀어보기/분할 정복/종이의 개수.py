import sys
input = sys.stdin.readline

N = int(input())

P = [list(map(int, input().split())) for _ in range(N)]

def Check(paper, n):
    global count_0
    global count_1
    global count_2
    
    c_0 = 0
    c_1 = 0
    c_2 = 0
    for p in paper:
        c_0 = c_0 + p.count(0)
        c_1 = c_1 + p.count(1)
        c_2 = c_2 + p.count(-1)

    if c_0 == n**2 or c_1 == n**2 or c_2 == n**2:
        if c_0 == n**2:
            count_0 += 1
        elif c_1 == n**2:
            count_1 += 1
        else:
            count_2 += 1            
        return    
    else:
        for h in range(3):
            for w in range(3):
                Check([p[(n//3)*w:(n//3)*(w+1)] for p in paper[(n//3)*h:(n//3)*(h+1)]], n//3)

count_0 = 0     
count_1 = 0
count_2 = 0

Check(P, N)

print(count_2)
print(count_0)
print(count_1)
        