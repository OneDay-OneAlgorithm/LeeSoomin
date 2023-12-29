# 배열 제어하기

def solution(arr):
  new_arr = list(set(arr))
  new_arr.sort(reverse=True)
  return new_arr
  

print(solution([4,2,2,1,3,4]))