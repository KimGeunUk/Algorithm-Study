import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    l = list(map(int, input().split()))
    
    s = 0
    for i in range(1, l[0]+1):
        s += l[i]
    avg = s/l[0]
    
    c = 0
    for i in range(1, l[0]+1):
        if avg < l[i]:
            c += 1
            
    print('{:.3f}%'.format(c/l[0]*100))