# 여기의 핵심은 수학 계산 식
# 의상종류 + 1 => 여기서 1은 안입는 경우이다. 마지막에 뺄셈하는 -1은 모두 벗은경우
# (a의상종류 + 1) * (b의상종류 +1) * ... - 1

def solution(clothes):
    dic = {}
    res = 1
    for i in clothes:
        key = i[1]
        dic[key] = dic.get(key,1) + 1
    for j in dic:
        res *= dic[j]
    return res - 1
