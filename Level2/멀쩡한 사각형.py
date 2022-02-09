import math

def gcd(w, h):      # 최대 공약수
    for i in range(min(w, h), 0, -1):
        if w % i == 0 and h % i == 0:
            return i

def solution(w, h):
    multi = w * h

    w, h = min(w, h), max(w, h)

    if w == 1 or h == 1:
        return 0
    elif w == h:
        return multi - w
    else:
        w_d, h_d = w / gcd(w, h), h / gcd(w, h)
        div = math.ceil(h_d / w_d)
        quo = h_d % w_d

        if quo != 0:
            sub = div * w_d * gcd(w, h) + (quo - 1) * gcd(w, h)
        else:
            sub = div * w_d * gcd(w, h)

        return int(multi - sub)

# 모범 답안 --------------------------------------------------------------------------------------------------------

def gcd_a(a, b):
    if a==0:
        return b
    else:
        gcd_a(b % a, a)

def solution_a(w,h):
    return w*h-w-h+gcd(w,h)



print(solution(8, 12))      # 80
print(solution(3, 9))      # 20
print(solution(10, 5))