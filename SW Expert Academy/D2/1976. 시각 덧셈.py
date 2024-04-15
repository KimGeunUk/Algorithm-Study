T = int(input())

for i in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    
    m_div, m_mod = divmod(m1 + m2, 60)
    
    h_div, h_mod = divmod(h1 + h2 + m_div, 12)
    
    if h_mod == 0: h_mod = 12
    
    print(f'#{i} {h_mod} {m_mod}')