# 하룻동안 만지작 거렸는데 풀지 못하였다.
# 모든 경우의 수를 생각하면 시간복잡도가 너무 높을 것 같아 생각조차 하지않았다..(대충 생각한게 잘못이다)
# 다른사람의 풀이를 배워 내 것으로 만들어야 겠다.

# DFS 또는 BFS 방법으로 풀이가 가능하다.
# numbers의 숫자들을 더할경우, 뺄경우를 생각하여 트리 형식으로 나타낸다.

# BFS
# numbers의 숫자를 더하거나 뺸 경우를 수평적으로 추가한다.
# result에 모든 계산 결과가 담기게 된다.
def solution1(numbers, target):
    answer = 0 
    results = [0]
    
    for num in numbers:
        tmp = []
        for parent in results:
            tmp.append(parent + num)
            tmp.append(parent - num)
        results = tmp
    
    for result in results:
        if result == target:
            answer += 1
    
    return answer

# DFS
# BFS는 수평적으로 더해 한꺼번에 모든 결과를 얻었다. DFS에서는 하나씩 확인한다.
# depth를 통해 트리의 깊이를 함께 알 수 있다.
# 트리의 끝에 도달하면 target 값과 비교해 정답 갯수를 구한다.
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer

print(solution([1, 1, 1, 1, 1], 3))     # 5
print(solution([4, 1, 2, 1], 4))        # 2