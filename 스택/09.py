# 10진수를 2진수로 변환하기

def solution(s):
  stack = []
  answer = ''

  while s != 0:
    stack.append(str(s % 2))
    s = s // 2
  
  while stack:
    answer += stack.pop()

  print(answer)

solution(10)
