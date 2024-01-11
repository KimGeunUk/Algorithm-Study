N = int(input())

answer = []

def hanoi(n, start, end, via):
    if n == 1:
        answer.append([start, end])
        return
    
    hanoi(n-1, start, via, end)

    answer.append([start, end])
    
    hanoi(n-1, via, end, start)
    
hanoi(N, 1, 3, 2)

print(len(answer))

for a in answer:
    print(str(a[0]) + ' ' + str(a[1]))