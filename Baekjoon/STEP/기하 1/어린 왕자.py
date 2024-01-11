import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split()) # 출발점 x1, y1 / 도착점 x2, y2
    
    N = int(input()) # 행성의 개수
    
    answer = 0
    for _ in range(N):
        cx, cy, cr = map(int, input().split())
        
        dis = cr ** 2        
        x1_dis = (x1 - cx) ** 2 + (y1 - cy) ** 2
        x2_dis = (x2 - cx) ** 2 + (y2 - cy) ** 2
        
        if dis > x1_dis and dis > x2_dis:
            continue
        
        elif dis > x1_dis:
            answer += 1
        
        elif dis > x2_dis:
            answer += 1
        
    print(answer)