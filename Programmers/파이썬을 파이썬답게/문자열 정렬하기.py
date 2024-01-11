# 다른 언어
def solution(str1):
    s, n = str1.strip().split(' ')
    n = int(n)
    l = n-len(s)
    
    print(s+' '*l)
    print(' '*int(l/2)+s+' '*int(l/2))
    print(' '*l+s)


# ljust, center, rjust
def solution(str1):
    s, n = str1.strip().split(' ')
    n = int(n)
    
    print(s.ljust(n))
    print(s.center(n))
    print(s.rjust(n))

print(solution('abc 7'))