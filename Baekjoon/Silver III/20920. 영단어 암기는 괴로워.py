import sys
input = sys.stdin.readline

from collections import Counter

n, m = map(int, input().split())

words = []

for _ in range(n):
    word = input().strip()
    
    if len(word) >= m:
        words.append(word)

words = [[k, v] for k, v in Counter(words).items()]

for word, _ in sorted(words, key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(word)