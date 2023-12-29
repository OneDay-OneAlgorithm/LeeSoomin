# 두개 뽑아서 더하기

def solution(numbers):
    answer = []
    for a in range(len(numbers)):
        for b in range(len(numbers)):
            if a != b:
                answer.append(numbers[a]+numbers[b])
    answer = list(set(answer))
    answer.sort()
    return answer