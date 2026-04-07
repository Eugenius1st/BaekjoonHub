from collections import deque
import math
# 배포 가능 날 베역 [7 5 9]
# 배포가능날 보다 작은 날들 묶음 (ex: 7보다 작은수 pop, 큰수 나왔을때 9보다 작은 수 pop)
def solution(progresses, speeds):
    deployDays = deque([])
    answer = []
    
    for i in range(len(progresses)):
        deployDay = math.ceil((100 - progresses[i]) / speeds[i])
        # 무조건 올림이어야 함!!!
        # print(100 - progresses[i], speeds[i])
        deployDays.append(deployDay)
    # print(deployDays)
    
    yageun = deployDays.popleft() # yageun = 개발 오래걸리는 날
    deployFunc = 1
    
    while len(deployDays) > 0: # python에서 while은 소문자임!
        # print("len(deployDays)", len(deployDays))
        tmp = deployDays.popleft()
        if tmp > yageun:
            answer.append(deployFunc)
            
            yageun = tmp # 초기화
            deployFunc = 1 # 초기화
        else:
            deployFunc += 1
    else: answer.append(deployFunc)
    
    return answer
            