T = int(input())

for i in range(T):
    candy = list(map(int, input().split()))
    
    count = 0
    for idx in range(len(candy)-1, 0, -1):
        if candy[idx] <= candy[idx-1]:
            print(candy[idx], candy[idx-1])
            n = candy[idx-1] - candy[idx] + 1
            candy[idx-1] -= n
            count += n
            
            if candy[idx-1] == 0:
                count = -1
                break

    print(f'#{i+1} {count}')
        