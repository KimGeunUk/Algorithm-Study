import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    string = input().strip()
    len_string = len(string)
    
    i = 0
    while i < len_string:
        if (97 <= ord(string[i]) <= 122):
            i += 1
        else:
            for j in range(i+1, len_string+1):
                if j < len(string) and (97 <= ord(string[j]) <= 122):
                    break

            numbers.append(int(string[i:j]))
            i = j + 1
numbers.sort()

for number in numbers:
    print(number)