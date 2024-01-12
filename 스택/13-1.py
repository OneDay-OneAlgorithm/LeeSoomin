# 오큰수

import sys
import copy
from collections import deque

N = int(sys.stdin.readline())
A = deque(list(map(int, sys.stdin.readline().split(' '))))
result = []

for _ in range(len(A)):
  a = A.popleft()
  stack = deque(copy.deepcopy(A))

  while stack:
    if stack[0] > a:
      result.append(stack[0])
      break
    else:
      stack.popleft()
  
  if len(stack) == 0:
    result.append(-1)

for r in result:
  print(r, end=' ')