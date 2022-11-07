# from collections import Counter as c
# word = input()

# max_k = ''
# max_v = -float('inf')
# count = sorted(c(word.upper()).items(), key=lambda x: -x[1])

# for k, v in count:
#     if v > max_v:
#         max_k = k
#         max_v = v
#     elif v == max_v:
#         print('?')
#         break
# else:
#     print(max_k)    

word = input().upper()
w = list(set(word))

cnt = []
for w_ in w:
    c = word.count(w_)
    cnt.append(c)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(w[(cnt.index(max(cnt)))])

