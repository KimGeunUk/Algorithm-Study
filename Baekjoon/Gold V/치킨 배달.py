import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

houses = []
chickens = []

for r in range(n):
    infos = map(int, input().split())
    for c, info in enumerate(infos):
        if info == 1:
            houses.append([r, c])
        elif info == 2:
            chickens.append([r, c])

chicken_score = []

for combies in combinations(chickens, m):

    house_score = [n*2 for _ in range(len(houses))]

    for combie in combies:
        for idx, house in enumerate(houses):
            house_score[idx] = min(house_score[idx], abs(combie[0] - house[0]) + abs(combie[1] - house[1]))
        
    chicken_score.append(sum(house_score))

print(min(chicken_score))
