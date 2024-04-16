T = int(input())

for i in range(T):
    N = int(input())

    distance = 0
    speed = 0
    
    for _ in range(N):
        command = input().strip()

        if command[0] != '0':
            if command[0] == '1':
                speed += int(command[2])
                distance += speed
            elif command[0] == '2':
                speed -= int(command[2])
                if speed < 0: speed = 0
                distance += speed
        else:
            distance += speed
    
    print(f'#{i+1} {distance}')