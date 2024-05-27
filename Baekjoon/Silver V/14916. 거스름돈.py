n = int(input())

answer = 0

while n > 0:
    if n % 5 == 0:
        answer += n // 5
        n %= 5
        break
    else:
        n -= 2
        answer += 1
    
if n != 0:
    answer = -1

print(answer)
    

"""
n = int(input())
arr = [-1 for _ in range(n+1)]

if n >= 2: arr[2] = 1
if n >= 4: arr[4] = 2
if n >= 5: arr[5] = 1

for i in range(6, n+1):
    if arr[i-2] != -1 and arr[i-5] != -1:
        arr[i] = min(arr[i-2] + 1, arr[i-5] + 1)
    elif arr[i-2] != -1:
        arr[i] = arr[i-2] + 1

print(arr[-1])
"""