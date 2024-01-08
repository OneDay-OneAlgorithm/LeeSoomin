# 괄호 회전하기

import copy

def solution(s):
    answer = 0
    sLen = len(s)
    
    for i in range(sLen):
        stack = []
        for j in range(sLen):
            c = s[(i+j)%sLen]
            
            if c == '(' or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    break
                
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
    
    return answer