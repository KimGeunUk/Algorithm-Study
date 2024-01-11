N = int(input())

room = []
for i in range(N):
    x, y = map(int, input().split())
    room.append([x, y])

# 가장 빨리 끝나고, 가장 빨리 시작하여야 한다.
# x[1]을 먼저 정렬하고 x[0]을 다음으로 정렬한다.
sort_room = sorted(room, key = lambda x:(x[1],x[0]))

end = 0
count = 0
for i in range(N):
    if end <= sort_room[i][0]:
        count += 1
        end = sort_room[i][1]
    

print(count)