T = int(input())

for t in range(T):
    S = input().strip()
    lenS = len(S)
    
    print('..#', end='')
    for _ in range(lenS-1):
        print('...#', end='')
    print('..')
    
    for _ in range(lenS):
        print('.#.#', end='')
    print('.')
    
    for s in S:
        print(f'#.{s}.', end='')
    print('#')
    
    for _ in range(lenS):
        print('.#.#', end='')
    print('.')
    
    print('..#', end='')
    for _ in range(lenS-1):
        print('...#', end='')
    print('..')