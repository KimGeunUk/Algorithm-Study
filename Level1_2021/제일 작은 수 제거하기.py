def solution(arr):
    answer = []

    mina = 9999

    for i in arr:
        mina = min(i, mina)

    arr.remove(mina)

    if len(arr) == 0:
        arr.append(-1)        

    answer = arr
    
    return answer

print(solution([4,3,2,1]))
print(solution([10]))