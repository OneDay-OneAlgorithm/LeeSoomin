# 모의고사

def solution(answers):
    answer = []
    count = [0,0,0]
    pattern = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for a in range(len(answers)):
        for p in range(len(pattern)):
            if pattern[p][((a+1)%len(pattern[p]))-1] == answers[a]:
                count[p] += 1
    
    for a in range(len(count)):
        if count[a] == max(count):
            answer.append(a+1)
    
    return answer