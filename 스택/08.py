# 괄호 짝 맞추기

from collections import deque

def solution(s):
  stack = deque([])
  for i in s:
    stack.append(i)
  answer = 0
  
  while stack:
    cur = stack.popleft()

    if cur == '(':
      answer += 1
    elif cur == ')':
      answer -= 1
  
  if answer == 0:
    return True
  else: 
    return False