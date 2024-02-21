import sys
input = sys.stdin.readline

N = int(input())

P = [list(map(int, input().split())) for _ in range(N)]

def Check(paper, n):
    global count_0
    global count_1
    
    c_0 = 0
    for p in paper:
        c_0 = c_0 + p.count(0)

    if c_0 == 0 or c_0 == n**2:
        if c_0 == 0:
            count_1 += 1
        else:
            count_0 += 1
            
        return    
    else:
        paper1 = [p[:n//2] for p in paper[:n//2]]
        Check(paper1, n//2)
        paper2 = [p[n//2:] for p in paper[:n//2]]
        Check(paper2, n//2)
        paper3 = [p[:n//2] for p in paper[n//2:]]
        Check(paper3, n//2)
        paper4 = [p[n//2:] for p in paper[n//2:]]
        Check(paper4, n//2)

count_0 = 0     
count_1 = 0

Check(P, N)

print(count_0)
print(count_1)
        