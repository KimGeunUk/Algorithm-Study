import sys
input = sys.stdin.readline

# 가장 긴 연속 부분
def longest_increasing_subsequence(arr: list):
    max_ = 0
    
    # 행
    for y in range(N):
        cnt = 1
        prev = arr[y][0]
        
        for next in arr[y][1:]:
            if prev == next:
                cnt += 1
            else:
                prev = next
                cnt = 1            
            max_ = max(max_, cnt)
    
    # 열
    temp = list(map(list, zip(*arr)))
    
    for y in range(N):
        cnt = 1
        prev = temp[y][0]
        
        for next in temp[y][1:]:
            if prev == next:
                cnt += 1
            else:
                prev = next
                cnt = 1            
            max_ = max(max_, cnt)
        
    return max_

N = int(input())

arr = [list(input().strip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_ = 0

for y in range(N):
    for x in range(N):
        if visited[y][x]: continue
        visited[y][x] = True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if -1 < nx < N and -1 < ny < N and visited[ny][nx] == False:
                if arr[y][x] != arr[ny][nx]:
                    arr[y][x] , arr[ny][nx] = arr[ny][nx], arr[y][x]
                    
                    value = longest_increasing_subsequence(arr)
                    max_ = max(max_, value)
                    
                    arr[y][x] , arr[ny][nx] = arr[ny][nx], arr[y][x]

print(max_)