import sys
from itertools import combinations

def solution(n):
    num = n
    answer = 0
    remainN = 0
    tmpN = ''
    multiN = 0
    while num > 0 :
        remainN = num %3
        num = num // 3
        tmpN += str(remainN)

    num = int(tmpN)

    while num > 0:
        remainN = num % 10
        num = num // 10
        answer += remainN * (3**multiN)
        multiN+=1

    return answer