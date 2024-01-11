def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.remove(g)
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.remove(g)
        else:
            return "No"
    else:
        return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]	))