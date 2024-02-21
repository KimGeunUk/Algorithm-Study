import sys
input = sys.stdin.readline

T = int(input())
    
for i in range(T):
    H, W, N = map(int, input().split())
    
    ROOM_X = (N-1) // H + 1
    ROOM_Y = (N-1) % H + 1
    
    print(ROOM_Y*100 + ROOM_X)
