import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input().rstrip() # Parenthesis String
    
    L = list()
    for p in ps:
        if len(L) == 0:
            L.append(p)
        else:
            if p == "(":
                L.append(p)
            else:
                if L[-1] == "(":
                    L.pop()
                else:
                    L.append(p)

    if len(L) == 0:
        print("YES")
    else:
        print("NO")