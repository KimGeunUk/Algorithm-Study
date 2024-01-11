def star_(n):
    if n == 1:
        return ['*']
    
    stars = star_(n//3)
    
    star = []
    
    for s in stars:
        star.append(s*3)
    
    for s in stars:
        star.append(s + ' '*(n//3) + s)
   
    for s in stars:
        star.append(s*3)

    return star

N = int(input())

print('\n'.join(star_(N)))