T = int(input())

for i in range(T):
    N = int(input())
    
    string = ''
    for _ in range(N):
        alphabet, length = input().strip().split()
        string += alphabet * int(length)
    
    print(f'#{i+1}', end='')
    for idx, alphabet in enumerate(string):
        if idx % 10 == 0:
            print()
            print(alphabet, end='')
        else:
            print(alphabet, end='')
    print()
            
        