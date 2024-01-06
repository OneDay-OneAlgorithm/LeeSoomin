# 괄호 짝 맞추기

from collections import deque

def solution(s):
  stack = deque([])
  
  for cur in s:
    if cur == '(':
      stack.append(cur)
    elif cur == ')':
      if stack:
        stack.pop()
  
  if stack:
    return False
  else: 
    return True