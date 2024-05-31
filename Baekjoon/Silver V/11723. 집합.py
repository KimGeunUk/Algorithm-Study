import sys
input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    orders = input().split()
    
    order = orders[0]
    if len(orders) > 1:
        num = int(orders[1])
    
    if order == 'add':
        S.add(num)
    elif order == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif order == 'remove':
        if num in S:
            S.remove(num)
    elif order == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif order == 'all':
        S = {i for i in range(1, 21)}
    elif order == 'empty':
        S.clear()