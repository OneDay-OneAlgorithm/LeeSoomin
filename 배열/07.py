# 방문 길이

def solution(dirs):
    x, y = 0, 0
    matrix = [[[] for _ in range(11)] for __ in range(11)]
    checkArr = [['U', 'y', 1], ['L', 'x', -1], ['R', 'x', 1], ['D', 'y', -1]]
    answer = 0
    
    for d in dirs:
        if d == 'R':
            if (x+1) <= 5:
                if [x+1+5, y+5] not in matrix[x+5][y+5] and [x+5,y+5] not in matrix[x+1+5][y+5]:
                    matrix[x+5][y+5].append([x+1+5, y+5])
                    matrix[x+1+5][y+5].append([x+5, y+5])
                    answer += 1
                x = x + 1
            continue
        if d == 'L':
            if (x-1) >= -5:
                if [x-1+5, y+5] not in matrix[x+5][y+5] and [x+5,y+5] not in matrix[x-1+5][y+5]:
                    matrix[x+5][y+5].append([x-1+5, y+5])
                    matrix[x-1+5][y+5].append([x+5, y+5])
                    answer += 1
                x = x - 1
            continue
        if d == 'U':
            if (y+1) <= 5:
                if [x+5, y+1+5] not in matrix[x+5][y+5] and [x+5,y+5] not in matrix[x+5][y+1+5]:
                    matrix[x+5][y+5].append([x+5, y+1+5])
                    matrix[x+5][y+1+5].append([x+5, y+5])
                    answer += 1
                y = y + 1
            continue
        if d == 'D':
            if (y-1) >= -5:
                if [x+5, y-1+5] not in matrix[x+5][y+5] and [x+5,y+5] not in matrix[x+5][y-1+5]:
                    matrix[x+5][y+5].append([x+5, y-1+5])
                    matrix[x+5][y-1+5].append([x+5, y+5])
                    answer += 1
                y = y - 1
            continue
                    
    return answer