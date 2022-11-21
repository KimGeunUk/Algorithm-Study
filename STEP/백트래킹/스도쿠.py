
def dfs(maps, idx):
    if idx >= len(zero_map):
        return True # 한 경우의 수가 다 끝났는지 체크
    
    y, x = zero_map[idx]    
               
    rows = maps[y][:]  # 행 
    colums = [m[x] for m in maps]# 열
    blocks = sum([m[int(x//3)*3:int(x//3)*3+3] for m in maps[int(y//3)*3:int(y//3)*3+3]], []) # 블록

    for num in list(set(stand) - set(rows + colums + blocks)):
        maps[y][x] = num        
        if dfs(maps, idx+1): return True # 한 경우의 수가 다 끝나고 더 진행 할 수 있는지 체크
        maps[y][x] = 0
    else:
        return False

maps = [list(map(int, input().split())) for _ in range(9)]
zero_map = [[i, j] for i in range(9) for j in range(9) if maps[i][j] == 0]

stand = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dfs(maps, 0)

print()
for m in maps:
    print(*m)
            
# # while True:
# #     if (sum(maps, [])).count(0) != 0:
# #         dfs(maps, 0, 0)

# #         for m in maps:
# #             print(*m)
# #     else:
# #         for m in maps:
# #             print(*m)
# #         break
