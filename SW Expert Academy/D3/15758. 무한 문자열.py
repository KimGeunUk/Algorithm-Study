def gcd(a, b):
    a, b = min(a,b), max(a, b)
    
    while b:
        a, b = b, a % b
    
    return a

T = int(input())

for t in range(T):
    S1, S2 = input().strip().split()
    
    lcm = len(S1) * len(S2) // gcd(len(S1), len(S2))
    
    if S1 * (lcm // len(S1)) == S2 * (lcm // len(S2)):
        print(f'#{t+1} yes')
    else:
        print(f'#{t+1} no')