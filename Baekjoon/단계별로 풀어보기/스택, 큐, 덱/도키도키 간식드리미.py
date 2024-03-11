import sys
input = sys.stdin.readline

n = int(input())

tmp = []
end = [0]
now = list(map(int, input().split()))[::-1]

while now or tmp:
    
    if now and (end[-1] + 1 == now[-1]):
        end.append(now.pop())
    elif tmp and (end[-1] + 1 == tmp[-1]):
        end.append(tmp.pop())        
    elif now:
        tmp.append(now.pop())
    else:
        break

if tmp: print("Sad")
else: print("Nice")