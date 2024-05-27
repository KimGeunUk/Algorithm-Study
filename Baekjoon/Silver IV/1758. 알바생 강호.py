import sys
input = sys.stdin.readline

n = int(input())

tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)

answer = 0

for i, tip in enumerate(tips, start=1):
    money = tip - (i - 1)
    if money < 0: continue
    answer += money

print(answer)