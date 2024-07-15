import sys
input = sys.stdin.readline

N = int(input()) # 스위치 수
switches = list(map(int, input().split()))
M = int(input()) # 학생 수

for _ in range(M):
    s, n = map(int, input().split())
    
    if s == 1: # 남
        for idx, switch in enumerate(switches, start=1):
            if idx % n == 0:
                if switches[idx-1] == 1:
                    switches[idx-1] = 0
                else:
                    switches[idx-1] = 1
    else: # 여
        st, ed = n-2, n
        
        while st > -1 and ed < N:
            if switches[st] == switches[ed]:
                st -= 1
                ed += 1
            else:
                break
        
        for idx in range(st+1, ed):
            if switches[idx] == 1:
                switches[idx] = 0
            else:
                switches[idx] = 1

for idx, switch in enumerate(switches, start=1):
    if idx != 1 and idx % 20 == 0:
        print(switch)
    else:
        print(switch, end=' ')