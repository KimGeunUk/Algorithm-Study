from collections import deque

def solution(x, y, n):
    answer = 0
    
    arr = deque([x])
    check = [0] * 1000001
    if x == y: return 0
        
    while True:
        answer += 1

        for _ in range(len(arr)):
            num = arr.popleft()
            
            first = num + n
            second = num * 2
            third = num * 3
            
            if first == y or second == y or third == y:
                return answer
            else:
                if first < y and check[first] == 0:
                    arr.append(first)
                    check[first] = 1
                if second < y and check[second] == 0:
                    arr.append(second)
                    check[second] = 1
                if third < y and check[third] == 0:
                    arr.append(third)
                    check[third] = 1
        
        if len(arr) == 0:
            return -1

# print(solution(10, 40, 5)) # 2
# print(solution(10, 40, 30)) # 1
# print(solution(2, 5, 4)) # -1
print(solution(10, 50, 5)) # -1
