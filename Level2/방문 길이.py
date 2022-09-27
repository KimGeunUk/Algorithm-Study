""" 
문제 설명
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
    U: 위쪽으로 한 칸 가기
    D: 아래쪽으로 한 칸 가기
    R: 오른쪽으로 한 칸 가기
    L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 
좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 
예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. 
(8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

제한사항 :
dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
dirs의 길이는 500 이하의 자연수입니다.

"""

def solution(dirs):
    answer = 0
    
    # U D R L
    mv = {'U': [0, -1], 'D': [0, 1], 'R': [1, 0], 'L': [-1, 0]}
    
    map_ = [[0 for _ in range(11)] for _ in range(11)]
    
    nx = 5
    ny = 5
    
    map_[ny][nx] = 1
    visited = []
    for idx, i in enumerate(dirs):    
        if nx + mv[i][0] < 0 or ny + mv[i][1] < 0 or nx + mv[i][0] > 10 or ny + mv[i][1] > 10:
            continue
        
        nx += mv[i][0]
        ny += mv[i][1]
        
        if map_[ny][nx] == 0:
            answer += 1
            map_[ny][nx] = 1     
            move = sorted([(nx, ny), (nx - mv[i][0], ny - mv[i][1])])
            visited.append(move)       
        else:
            map_[ny][nx] += 1
            move = sorted([(nx, ny), (nx - mv[i][0], ny - mv[i][1])])                
            if move not in visited:
                answer += 1
                visited.append(move) 

 
    return answer

print(solution("ULURRDLLU")) # 7
print(solution("UDU")) 
print(solution("LULLLLLLU")) # 7
print(solution("LURDLURDLURDLURDRULD")) # 7
print(solution("UUUUDUDUDUUU")) # 5