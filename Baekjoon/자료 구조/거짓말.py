import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = 0

know = list(map(int, input().split()))
know_truth = set(know[1:])
parties = [set(list(map(int, input().split()[1:]))) for _ in range(m)]

while True:
    for party in parties:
        if len(know_truth & party) > 0:
            know_truth |= party
            parties.remove(party)
            break
    else:
        break

for attend in parties:
    if len(attend & know_truth) == 0:            
        answer += 1

print(answer)

""" 
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
"""   