participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


def solution(participant, completion):

    participant = sorted(participant)
    completion = sorted(completion)

    for i, j in zip(participant, completion):
        if i != j:
            return i

    return participant[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

#유효성 검사 실패