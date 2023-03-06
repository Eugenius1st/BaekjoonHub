# DFS
# visited = []

# def DFS(node,computers):
#     for x in range(len(computers[node])):
#         if x != node and computers[node][x]==1 and x not in visited:
#             visited.append(x)
#             DFS(x,computers)
    

# def solution(n, computers):
#     answer = 0
#     for i in range(n):
#         if i not in visited:
#             answer+=1
#             visited.append(i)
#             DFS(i,computers)

#     return answer


# BFS
from collections import deque

def BFS(node,computers,visited,n):
    visited.append(node)
    haveToVisit = deque([])
    haveToVisit.append(node)
    while haveToVisit:
        tmpNum = haveToVisit.popleft()
        visited.append(tmpNum)
        for x in range(n):
            if x != tmpNum and computers[tmpNum][x]==1 and x not in visited:
                haveToVisit.append(x)
        
    

def solution(n, computers):
    visited = []
    answer = 0
    for i in range(n):
        if i not in visited:
            answer+=1
            BFS(i,computers,visited,n)
    print(answer)
    return answer
# 테스트 1
# 입력값 〉 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# 기댓값 〉 2
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 2
# 입력값 〉 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# 기댓값 〉 1
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 3
# 입력값 〉 4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
# 기댓값 〉 4
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 4
# 입력값 〉 4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
# 기댓값 〉 1
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 5
# 입력값 〉 3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
# 기댓값 〉 2
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 6
# 입력값 〉 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# 기댓값 〉 1
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 7
# 입력값 〉 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# 기댓값 〉 2
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 8
# 입력값 〉 4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
# 기댓값 〉 1
# 실행 결과 〉 테스트를 통과하였습니다.
# 테스트 9
# 입력값 〉 7, [[1, 0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1, 1]]
# 기댓값 〉 1
# 실행 결과 〉 테스트를 통과하였습니다.