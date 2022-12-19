import sys
input = sys.stdin.readline

from collections import deque

N = int(input()) # buffer size

packet = deque()

while True:
    info_ = int(input())
        
    if info_ == -1:
        break
    
    if info_ == 0:
        packet.popleft()
    elif info_ != 0 and len(packet) < N:
        packet.append(info_)

if packet:
    print(*packet)
else:
    print('empty')