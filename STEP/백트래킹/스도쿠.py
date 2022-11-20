
def dfs(maps, y, x):
    if x > 8 and y > 8:
        return
    
    if maps[y][x] == 0:
        rows = maps[y][:]  # 행
        colums = [m[x] for m in maps]# 열
        blocks = sum([m[int(x//3)*3:int(x//3)*3+3] for m in maps[int(y//3)*3:int(y//3)*3+3]], []) # 블록
        
        print(list((set(stand) - set(rows)) & (set(stand) - set(colums) & (set(stand) - set(blocks)))))
            
    if x < 8 and y < 8:
        dfs(maps, y+1, x)
        dfs(maps, y, x+1)
        dfs(maps, y+1, x+1)
    elif x < 8 and y == 8:
        dfs(maps, y, x+1)
    elif x == 8 and y < 8:
        dfs(maps, y+1, x) 
    else:
        dfs(maps, x+1, y+1)

maps = [list(map(int, input().split())) for _ in range(9)]

stand = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dfs(maps, 0, 0)
print()
for m in maps:
    print(*m)
            
# while True:
#     if (sum(maps, [])).count(0) != 0:
#         dfs(maps, 0, 0)

#         for m in maps:
#             print(*m)
#     else:
#         for m in maps:
#             print(*m)
#         break