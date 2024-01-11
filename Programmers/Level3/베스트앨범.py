from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    album = defaultdict(list)
    album_sum = defaultdict(int)
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        album[g].append([p, idx])
        album_sum[g] += p
        
    for k, v in album.items():
        album[k] = sorted(v, key=lambda x: (x[0], -x[1]))
    
    album_sum = dict(sorted(album_sum.items(), key=lambda x: x[1]))
    
    while len(album_sum) > 0:
        k, _ = album_sum.popitem()
        
        if len(album[k]) >= 2:
            v = album[k]
            answer.append(v.pop()[1])
            answer.append(v.pop()[1])
        else:
            v = album[k]
            answer.append(v.pop()[1])
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500])) # [4, 1, 3, 0]