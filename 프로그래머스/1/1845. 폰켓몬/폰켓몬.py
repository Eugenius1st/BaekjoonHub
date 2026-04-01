def solution(nums):
    dic = {}
    
    # 종류 세기
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
    
    selectCnt = len(nums) // 2
    
    return min(len(dic), selectCnt)