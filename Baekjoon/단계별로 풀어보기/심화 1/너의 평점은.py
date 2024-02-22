import sys
input = sys.stdin.readline

grade_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P": 0.0
}

score_sum = 0
credit_sum = 0

for _ in range(20):
    subject, credit, grade = input().split()
    if grade == "P": continue
    score_sum += float(credit) * grade_score[grade]
    credit_sum += float(credit)

print(f"{score_sum/credit_sum:.6f}")