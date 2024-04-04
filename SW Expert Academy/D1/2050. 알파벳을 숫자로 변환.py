alphabets = input().strip()

for alphabet in alphabets:
    print(ord(alphabet) - 64, end=' ')