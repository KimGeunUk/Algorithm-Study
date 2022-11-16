# def gcd(a, b):
#     a, b = min(a, b), max(a, b)
    
#     for i in range(a, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i
        
# def lcm(a, b):
#     a, b = min(a, b), max(a, b)
#     for i in range(b, (a*b)+1):
#         if i % a == 0 and i % b == 0:
#             return i

# def gcd(a, b):
#     a, b = min(a, b), max(a, b)
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     a, b = min(a, b), max(a, b)
#     return (a * b) // gcd(a, b)

import math

a, b = map(int, input().split()) 

print(math.gcd(a, b))
print(math.lcm(a, b))