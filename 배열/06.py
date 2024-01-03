# 실패율

def solution(N, stages):
    failArr = [0.0] * (N + 1)
    stageArr = [0] * (N + 1)
    clearArr = [0] * (N + 1)
    stageNum = [s for s in range(1, N + 1)]
    
    for s in stages:
        if s == N + 1:
            for k in range(1,s):
                stageArr[k] += 1
        else:
            for k in range(1,s+1):
                stageArr[k] += 1
        if s != N + 1:
            clearArr[s] += 1
        
    for n in range(1,N+1):
        if stageArr[n] != 0:
            print(clearArr[n], stageArr[n])
            failArr[n] = clearArr[n] / stageArr[n]
    
    stageNum.sort(key=lambda x: (failArr[x],-x), reverse=True)
    
    return stageNum