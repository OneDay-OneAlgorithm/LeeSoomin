# 주식 가격

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for p in range(len(prices)):
        for s in stack:
            s[1] += 1
            
        while stack and stack[-1][0] > prices[p]:
            poped = stack.pop()
            answer[poped[2]] = poped[1]
        
        stack.append([prices[p], 0, p])
        
    for s in stack:
        answer[s[2]] = s[1]
    
    return answer