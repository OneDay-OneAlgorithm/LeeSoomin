def solution(string):
    stack = []
    
    for s in string:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)   
    if stack:
        return 0
    else: 
        return 1