# 크레인 인형 뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves:
        m = m - 1 # 인덱스화
        N = len(board[0]) # 보드 길이
        
        i = 0
        get = 0
        
        while board[i][m] == 0 and i < N - 1:
            i += 1
        
        if board[i][m] == 0:
            continue
        
        get = board[i][m]
        board[i][m] = 0
        
        if stack and get == stack[-1]:
            stack.pop()
            answer += 2
        else:
            stack.append(get)
    
    return answer