import sys
input = sys.stdin.readline

op = input().strip()

arr = []
temp = []

for o in op:
    if arr == [] or o == "(" or o == "[":
        arr.append(o)
    else:
        p = arr.pop()
        if p == "(":
            if o == ")":
                temp.append(2)
            else:
                arr.append(p)
                arr.append(o)
        elif p == "[":
            if o == "]":
                temp.append(3)
            else:
                arr.append(p)
                arr.append(o)

    print(arr, temp)