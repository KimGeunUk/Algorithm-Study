import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

A.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for b in B:
    print(binary_search(A, b, 0, len(A)-1))
