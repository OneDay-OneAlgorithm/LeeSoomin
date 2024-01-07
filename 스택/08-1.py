# 스택 추가: 쇠막대기

import sys
from collections import deque

laser = sys.stdin.readline()
stack = deque([])
result = 0
laserSkip = False
laserDouble = False

for i in range(len(laser)):
  if laserSkip:
    laserSkip = False
    continue
  
  if laser[i] == '(':
    if laser[i+1] == ')':
      laserSkip = True
      result += len(stack)
    else:
      stack.append('(')
  elif laser[i] == ')':
    stack.pop()
    result += 1

print(result)
