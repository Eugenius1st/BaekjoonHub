import sys
from itertools import combinations

def solution(nums):
    answer = 0
    for x in combinations(nums,3):
        chPrime = x[0]+x[1]+x[2]
        for i in range(2,chPrime):
            if(chPrime%i==0): break
        else : answer+=1
    return answer