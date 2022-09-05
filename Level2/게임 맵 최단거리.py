"""
BFS
너비 우선 탐색으로 그래프에서 가까운 노드부터 우선적으로 탐색
Queue 를 이용해서 구현이 가능

1. 시작 노드를 큐에 넣고 방문 처리
2. 큐에서 노드를 꺼내고 인접 노드 중 방문하지 않은 노드를 큐에 넣고 방문 처리
3. 큐에 노드가 없을 때까지 2번 과정 반복
"""
from collections import deque
def solution(maps):
    answer = 0
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            # 상하좌우 칸 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵을 넘어갈 경우 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
                
                # 벽이면 무시
                if maps[nx][ny] == 0: continue
                
                # 처음 지나가는 길이면 거리 계산 후 다시 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny)) # 재귀

        # 상대 팀 진영 까지의 거리
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
                

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [0,0,0,0,1]])) # 11

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,0],
                [0,0,0,0,1]])) # -1