T = int(input())

for t in range(T):
    A, B, C, D = map(int, input().split())
    answer = ''

    if B == 0 and C == 0 and A != 0 and D != 0:
        answer = 'impossible'
    elif abs(B-C) > 1:
        answer = 'impossible'
    else:
        if B == 0 and C == 0:
            if A != 0: answer = '0' * (A + 1)
            else: answer = '1' * (D + 1)
        elif B < C:
            answer = '1' * D + '10' * C + '0' * A
        elif B > C:
            answer = '0' * A + '01' * B + '1' * D
        else:
            answer = '0' * A + '01' * B + '1' * D + '0'

    print(f'#{t+1} {answer}')