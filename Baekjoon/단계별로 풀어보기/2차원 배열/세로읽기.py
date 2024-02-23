import sys
input = sys.stdin.readline

arr = ["" for _ in range(15)]

for _ in range(5):
    words = list(input().strip())
    for idx, word in enumerate(words):
        arr[idx] += word
        
print(''.join(arr))
        