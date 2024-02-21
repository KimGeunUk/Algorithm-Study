import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_S = set()
M_S = set()

for _ in range(N):
    N_S.add(input().rstrip())

for _ in range(M):
    M_S.add(input().rstrip())    

intersection = sorted(N_S & M_S)
print(len(intersection))
for i in intersection:
    print(i)