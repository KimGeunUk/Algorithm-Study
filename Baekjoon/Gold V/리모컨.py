N = int(input())
M = int(input())

broken_button = []
if M > 0: broken_button = list(map(int, input().split()))
    
min_ = abs(100 - N)

for num in range(1000001):
    str_num = str(num)
    
    for i, n in enumerate(str_num):
        if int(n) in broken_button: break
    else:
        min_ = min(min_, abs(int(str_num) - N) + len(str_num))
        
print(min_)