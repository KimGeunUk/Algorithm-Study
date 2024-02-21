import sys
input = sys.stdin.readline

N = int(input())

M = []
for i in range(N):
    M.append(list(map(int, input.split())))

M = sorted(M,key = lambda x: (x[1], x[0]))

end, mcount = 0, 0
for i in range(N):
    if end <= M[i][0]:
        mcount += 1
        end = M[i][1]
print(mcount)