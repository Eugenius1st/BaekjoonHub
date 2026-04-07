def solution(arr):
    answer = []

    for i in arr:
        answerLastIdx = len(answer)-1
        if answerLastIdx >= 0 and answer[answerLastIdx] == i:
            continue
        else:
            answer.append(i)
        
    return answer