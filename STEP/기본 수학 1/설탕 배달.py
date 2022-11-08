N = int(input())

if (N - 3) % 5 == 0:
    answer = (N // 5) + (N % 5) // 3
elif (N - 5) % 3 == 0:
    answer = (N // 3) + (N % 3) // 5
elif N % 5 == 0:
    answer = N // 5
elif N % 3 == 0:
    answer = N // 3
else:
    answer = -1
    
print(answer)