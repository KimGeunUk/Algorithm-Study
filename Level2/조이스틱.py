import re

from regex import A

# def solution(name):
#     answer_list = []
        
#     for k in range(len(name)):
#         answer = 0
    
#         default_list = ['A' for i in name] * 2
#         name_list = [i for i in name] * 2

#         for idx, (i, j) in enumerate(zip(default_list[k:k+len(name)], name_list[k:k+len(name)])):
#             count = ord(j) - 65
            
#             default_list[idx+k] = chr(count+65)
            
#             if count > 13:            
#                 count = 26 - count
            
#             answer += count
            
#             if default_list[k:k+len(name)] == name_list[k:k+len(name)]:                
#                 break
            
#             answer += 1
        
#         answer_list.append(answer)
#     print(answer_list)

#     return min(answer_list)


# def solution(name):    
#     answer_list = []
    
#     # 정방향
#     answer = 0
#     default_list = ['A' for i in name]
#     name_list = [i for i in name]
#     for idx, i in enumerate(name_list):
#         count = ord(i) - 65
#         default_list[idx] = chr(count+65)
        
#         if count > 13:            
#             count = 26 - count
        
#         answer += count
        
#         if default_list == name_list:                
#             break
        
#         answer += 1
#     answer_list.append(answer)
#     # 역방향    
#     answer = 0
#     default_list = ['A' for i in name]
#     name_list = [name[0]]+[i for i in name[len(name):0:-1]]
#     for idx, i in enumerate(name_list):
#         count = ord(i) - 65
#         default_list[idx] = chr(count+65)
        
#         if count > 13:            
#             count = 26 - count
        
#         answer += count
        
#         if default_list == name_list:                
#             break
        
#         answer += 1
        
#     answer_list.append(answer)
    
#     if 'A' in name:
#         # 정방향 -> 역방향    
#         answer = 0    
#         Aindex = [i+1 for i, c in enumerate(name[1:]) if c == 'A']
#         name_list = [name[0]] + [i for i in name[1:Aindex[0]]]+ [i for i in name[Aindex[0]-2::-1]] + [i for i in name[len(name):Aindex[0]:-1]]
#         default_list = ['A' for i in name_list]
#         for idx, i in enumerate(name_list):
#             count = ord(i) - 65
#             default_list[idx] = chr(count+65)
            
#             if count > 13:            
#                 count = 26 - count
            
#             answer += count
            
#             if default_list == name_list:                
#                 break
            
#             answer += 1
#         answer_list.append(answer)
        
#         # 역방향 -> 정방향
#         answer = 0    
#         Aindex = [i+1 for i, c in enumerate(name[1:]) if c == 'A']
        
#         name_list = [i for i in name[len(name)-1:Aindex[-1]:-1]] + [name[0]] + [i for i in name[1:Aindex[-1]+1]]
#         default_list = ['A' for i in name_list]
        
#         for idx, i in enumerate(name_list): 
#             count = ord(i) - 65
#             default_list[idx] = chr(count+65)
                        
#             print(name_list)
#             print(default_list)

#             if count > 13:            
#                 count = 26 - count
            
#             answer += count  
                        
#             if default_list == name_list:                
#                 break
#             else:            
#                 answer += 1      

#             print(answer)

#         answer_list.append(answer)
#     print(answer_list)
#     return min(answer_list)

# # 다른사람 풀이

def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        print(left_moved, right_moved[0]+right_moved[:0:-1])
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            print(n)
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)
            answer = min(answer, row_move + col_move)

    return answer

# # 다른사람 풀이
# def solution(name):
#     answer = 0
#     n = len(name)

#     def alphabet_to_num(char):
#         num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
#         return num_char[ord(char) - ord('A')]

#     for ch in name:
#         answer += alphabet_to_num(ch)
    
#     move = n - 1
#     for idx in range(n):
#         next_idx = idx + 1
#         while (next_idx < n) and (name[next_idx] == 'A'):
#             next_idx += 1
#         distance = min(idx, n - next_idx)
#         move = min(move, idx + n - next_idx + distance)

#     answer += move
#     return answer

print(solution("JEROEN"))
print(solution("JAN"))
# print(solution("ABAAAAAAAAABB")) # 7
# print(solution("BBBBAAAAAB")) # 10
# print(solution("AAAAA")) # 0
# print(solution("ABABAAAAABA"))

"""
65                                                                        96
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
0 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1
"""