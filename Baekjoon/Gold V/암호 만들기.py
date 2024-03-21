import sys
input = sys.stdin.readline

from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())

words = sorted(input().strip().split())

for word in list(combinations(words, l)):
    vowel_count = 0
    consonant_count = 0
    
    for w in word:
        if w in vowels: vowel_count += 1
        else: consonant_count += 1
    
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(word))