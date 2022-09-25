""" 
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입력 형식 :
    입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
    2 ≦ n, m ≦ 30
    board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
"""

def solution(m, n, board):
    answer = 0
    
    mx = [1, 0, 1] # 오, 아, 대
    my = [0, 1, 1]
    
    board = [list(i) for i in board]
    while True:
        rm = []
        
        for i in range(m-1):
            for j in range(n-1):
                alpha = board[i][j]
                
                for k in range(3):
                    if alpha != board[i+my[k]][j+mx[k]]:
                        break
                    elif k == 2 and board[i][j] != '':
                        if [i, j] not in rm:
                            rm.append([i, j])
                            
                        for l in range(3):
                            if [i+my[l], j+mx[l]] not in rm:
                                rm.append([i+my[l], j+mx[l]])
        
        if len(rm) < 1:
            break
        
        answer += len(rm)
        
        for i in rm:
            print(i)
            if i[0] > 0: 
                for j in range(i[0], 0, -1):
                    board[j][i[1]] = board[j-1][i[1]]
                    board[j-1][i[1]] = ''
            else:
                board[i[0]][i[1]] = ''
                
        for i in board:
            print(i)
    return answer

#print(solution(4, 5, ["AAADE", "AAABF", "CCBBF", "CCBDE"]))
#print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(8 ,5 ,["HGNHU", 
                      "CRSHV",
                      "UKHVL",
                      "MJHQB",
                      "GSHOT",
                      "MQMJJ", 
                      "AGJKK",
                      "QULKK"]))