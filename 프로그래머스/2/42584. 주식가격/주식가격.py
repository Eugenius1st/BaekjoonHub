from collections import deque

def solution(prices):
    answer = [len(prices) - i -1 for i in range(len(prices))] # 4,3,2,1,0
    stocks = [(prices[idx], idx) for idx in range(len(prices))]
    isUp = deque([])
    isDown = [] # (idx,떨어진시점idx) 저장

    for i in range(len(stocks)):
        curStock = stocks[i] # [0] = 값, [1] = idx
        if(len(isUp))==0: 
            isUp.append(curStock)
            
        # 현재 주식 값이 isUp의 마지막 값이 보다 큰 경우
        elif isUp[-1][0] < curStock[0]:
            isUp.append(curStock)
        
        # 현재 주식 값이 isUp의 마지막 값이 보다 작은 경우
        else:
            while len(isUp) > 0 and isUp[-1][0] > curStock[0]:
                popedStock = isUp.pop()
                isDown.append((popedStock[1],i))
            isUp.append(curStock)     
        # print(isDown)
    for isDownTuple in isDown:
        answer[isDownTuple[0]] = isDownTuple[1] - isDownTuple[0]
    return answer