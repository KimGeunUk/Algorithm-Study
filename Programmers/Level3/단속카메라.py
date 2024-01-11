def solution(routes):
    answer = 0
    
    routes = sorted(routes, key=lambda x: x[1])

    # 제일 처음
    route = routes[0]
    s, e = route[0], route[1]
    answer += 1
    
    # 이후 끝 부분만 고려하면 된다 !
    for route in routes[1:]:        
        if e < route[0]:
            e = route[1]
            answer += 1

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) # 2
print(solution([[-20, 15], [-14,-5], [-18,-13], [-5,-3]])) # 2