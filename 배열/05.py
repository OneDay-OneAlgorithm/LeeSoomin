# 행렬의 곱셈

def solution(arr1, arr2):
    ab = [[0 for _ in range(len(arr2[0]))] for __ in range(len(arr1))]
    
    for y in range(len(ab)):
        for x in range(len(ab[0])):
            for count in range(len(arr1[0])):
                ab[y][x] += arr1[y][count] * arr2[count][x]
    return ab