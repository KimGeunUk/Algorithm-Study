T = int(input())

prime = [True for _ in range(1000)]
prime[0], prime[1] = False, False
for i in range(2, int(1000**0.5)+1):
    if prime[i]:        
        for j in range(i*i, 1000, i):
            prime[j] = False

for t in range(T):
    N = int(input())
    prime_num = [idx for idx, p in enumerate(prime[:N]) if p]
    
    L = set()
    for num1 in prime_num:
        for num2 in prime_num:
            num3 = N - (num1 + num2)
            if num3 > 0 and prime[num3]:
                L.add(tuple(sorted([num1, num2, num3])))
    print(f'#{t+1} {len(L)}')