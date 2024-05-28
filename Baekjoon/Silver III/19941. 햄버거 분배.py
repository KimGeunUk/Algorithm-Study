import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(input().strip())

count = 0
for i, ar in enumerate(arr):
    if ar == 'P':
        for j in range(K, 0, -1):        
            if i >= j and arr[i-j] == 'H':
                arr[i-j] = -1
                count += 1
                break
        else:
            for j in range(1, K+1):
                if i < N - j and arr[i+j] == 'H':
                    arr[i+j] = -1
                    count += 1
                    break

print(count)