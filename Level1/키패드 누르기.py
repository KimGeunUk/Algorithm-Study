def solution(numbers, hand):
    answer = ''

    lefthand = '*'
    righthand = '#'    
    
    countL = 0
    countR = 0
    Lhand = 0
    Rhand = 0

    for i in range(len(numbers)):

        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:

            answer += 'L'

            if numbers[i] == 1:
                lefthand = 1                
            elif numbers[i] == 4:
                lefthand = 4                
            else:
                lefthand = 7
                
            
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:

            answer += 'R'

            if numbers[i] == 3:
                righthand = 3                
            elif numbers[i] == 6:
                righthand = 6                
            else:
                righthand = 9
                
        
        elif numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0:

            if numbers[i] == 2:

                Lhand = lefthand
                Rhand = righthand

                if lefthand == 1:
                    countL = 1
                elif lefthand == 4:
                    countL = 2
                elif lefthand == 7:
                    countL = 3
                elif lefthand == 2:
                    countL = 0
                elif lefthand == 5:
                    countL = 1
                elif lefthand == 8:
                    countL = 2
                elif lefthand == 0:
                    countL = 3
                elif lefthand == '*':
                    countL = 4
                
                if righthand == 3:
                    countR = 1
                elif righthand == 6:
                    countR = 2
                elif righthand == 9:
                    countR = 3
                elif righthand == 2:
                    countR = 0
                elif righthand == 5:
                    countR = 1
                elif righthand == 8:
                    countR = 2
                elif righthand == 0:
                    countR = 3
                elif righthand == '#':
                    countR = 4
                
                if countL < countR:
                    answer += 'L'
                    lefthand = 2
                    righthand = Rhand
                elif countL > countR:
                    answer += 'R'
                    righthand = 2
                    lefthand = Lhand
                elif countL == countR:
                    if hand == 'right':
                        answer += 'R'
                        righthand = 2
                        lefthand = Lhand
                    else:
                        answer += 'L'
                        lefthand = 2
                        righthand = Rhand

                countL = 0
                countR = 0
            
            elif numbers[i] == 5:
                Lhand = lefthand
                Rhand = righthand

                if lefthand == 1:
                    countL = 2
                elif lefthand == 4:
                    countL = 1
                elif lefthand == 7:
                    countL = 2
                elif lefthand == 2:
                    countL = 1
                elif lefthand == 5:
                    countL = 0
                elif lefthand == 8:
                    countL = 1
                elif lefthand == 0:
                    countL = 2
                elif lefthand == '*':
                    countL = 3
                
                if righthand == 3:
                    countR = 2
                elif righthand == 6:
                    countR = 1
                elif righthand == 9:
                    countR = 2
                elif righthand == 2:
                    countR = 1
                elif righthand == 5:
                    countR = 0
                elif righthand == 8:
                    countR = 1
                elif righthand == 0:
                    countR = 2
                elif righthand == '#':
                    countR = 3
                
                if countL < countR:
                    answer += 'L'
                    lefthand = 5
                    righthand = Rhand
                elif countL > countR:
                    answer += 'R'
                    righthand = 5
                    lefthand = Lhand
                elif countL == countR:
                    if hand == 'right':
                        answer += 'R'
                        righthand = 5
                        lefthand = Lhand
                    else:
                        answer += 'L'
                        lefthand = 5
                        righthand = Rhand
                
                countL = 0
                countR = 0

            elif numbers[i] == 8:
                Lhand = lefthand
                Rhand = righthand

                if lefthand == 1:
                    countL = 3
                elif lefthand == 4:
                    countL = 2
                elif lefthand == 7:
                    countL = 1
                elif lefthand == 2:
                    countL = 2
                elif lefthand == 5:
                    countL = 1
                elif lefthand == 8:
                    countL = 0
                elif lefthand == 0:
                    countL = 1
                elif lefthand == '*':
                    countL = 2
                
                if righthand == 3:
                    countR = 3
                elif righthand == 6:
                    countR = 2
                elif righthand == 9:
                    countR = 1
                elif righthand == 2:
                    countR = 2
                elif righthand == 5:
                    countR = 1
                elif righthand == 8:
                    countR = 0
                elif righthand == 0:
                    countR = 1
                elif lefthand == '#':
                    countR = 2    
                
                if countL < countR:
                    answer += 'L'
                    lefthand = 8
                    righthand = Rhand
                elif countL > countR:
                    answer += 'R'
                    righthand = 8
                    lefthand = Lhand
                elif countL == countR:
                    if hand == 'right':
                        answer += 'R'
                        righthand = 8
                        lefthand = Lhand
                    else:
                        answer += 'L'
                        lefthand = 8
                        righthand = Rhand
                
                countL = 0
                countR = 0

            elif numbers[i] == 0:
                Lhand = lefthand
                Rhand = righthand

                if lefthand == 1:
                    countL = 4
                elif lefthand == 4:
                    countL = 3
                elif lefthand == 7:
                    countL = 2
                elif lefthand == 2:
                    countL = 3
                elif lefthand == 5:
                    countL = 2
                elif lefthand == 8:
                    countL = 1
                elif lefthand == 0:
                    countL = 0
                elif lefthand == '*':
                    countL = 1
                
                if righthand == 3:
                    countR = 4
                elif righthand == 6:
                    countR = 3
                elif righthand == 9:
                    countR = 2
                elif righthand == 2:
                    countR = 3
                elif righthand == 5:
                    countR = 2
                elif righthand == 8:
                    countR = 1
                elif righthand == 0:
                    countR = 0
                elif lefthand == '#':
                    countR = 1
                
                if countL < countR:
                    answer += 'L'
                    lefthand = 0
                    righthand = Rhand
                elif countL > countR:
                    answer += 'R'
                    righthand = 0
                    lefthand = Lhand
                elif countL == countR:
                    if hand == 'right':
                        answer += 'R'
                        righthand = 0
                        lefthand = Lhand
                    else:
                        answer += 'L'
                        lefthand = 0
                        righthand = Rhand

                countL = 0
                countR = 0                                    

    return answer

    # 20개 중에 1개가 오류가 나는데 모르겠다..

print(solution([0,2],'right'))

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))