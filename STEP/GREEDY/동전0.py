N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))
    
answer = 0
       
for i in coin[::-1]:
    if K >= i:
        answer += K//i
        K = K%i
    
print(answer)