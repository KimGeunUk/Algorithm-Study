from collections import deque

N = int(input())

card = deque([i for i in range(1, N+1)])

rm = True
while len(card) > 1:
    if rm:
        card.popleft()
        rm = False
    else:
        card.append(card.popleft())
        rm = True
else:
    print(card.popleft())