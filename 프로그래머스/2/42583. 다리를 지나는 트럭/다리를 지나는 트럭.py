from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights) # 대기중인 트럭
    bridge = deque([0 for _ in range(bridge_length)]) # 다리 스택
    answer = 0
    bridgeWeight = 0
    # push, pop 으로 하나씩 땡기고, sum은 쓰지 않는걸로?
    while trucks:
        answer += 1
        bridgeWeight -= bridge.popleft()
        # print(bridge)
        if len(trucks)>0 and bridgeWeight+trucks[0] <= weight:
            curTruck = trucks.popleft()
            bridgeWeight += curTruck
            bridge.append(curTruck)
        else:
            bridge.append(0)
            
    return answer+bridge_length