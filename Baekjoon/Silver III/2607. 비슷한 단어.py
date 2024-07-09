import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())

answer = 0

word = input().strip()
word_count = Counter(word)


for _ in range(N-1):
    new = input().strip()
    new_count = Counter(new)
    
    diff = 0
    
    union_word = set(word_count.keys()) | set(new_count.keys())
    
    for char in union_word:
        diff += abs(word_count[char] - new_count[char])
            
    if diff <= 2 and abs(len(word) - len(new)) <= 1:
        answer += 1
        
print(answer)

"""
8
DOG
GOD
GOOD
DOGL
GD
PGG
G
DOGOD
"""