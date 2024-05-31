N = int(input())
arr = input().strip()

start = arr[0]

if start == 'R':
    print(arr.count('RB') + 1)
else:
    print(arr.count('BR') + 1)