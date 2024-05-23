import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]
    

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b: parent[b] = a
    else: parent[a] = b

for _ in range(m):
    o, a, b = map(int, input().split())
    
    if o == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")

''' 시간 초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

set_num = [None] * (n+1)
set_list = []

for _ in range(m):
    x, a, b = map(int, input().split())

    if set_num[a] == None:
        set_list.append({a})
        set_num[a] = len(set_list) - 1
        a_idx = set_num[a]
    else:
        a_idx = set_num[a]
    
    if set_num[b] == None:
        set_list.append({b})
        set_num[b] = len(set_list) - 1
        b_idx = set_num[b]
    else:
        b_idx = set_num[b]
    
    a_idx, b_idx = min(a_idx, b_idx), max(a_idx, b_idx)
    if x == 0:
        set_list[a_idx] = set_list[a_idx] | set_list[b_idx]
        
        if a_idx != b_idx:
            for num in set_list[b_idx]:
                set_num[num] = a_idx

            set_list[b_idx] = None
        
    elif x == 1:
        if set_list[a_idx] == set_list[b_idx]:
            print("YES")
        else:
            print("NO")
'''