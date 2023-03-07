from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def BFS(queue,maps,limitCol,limitRow,visited):
    visited[0][0]=True
    while queue:
        tmpXY = queue.popleft()
        tmpX = tmpXY[0]
        tmpY = tmpXY[1]
        if tmpXY == (limitRow-1,limitCol-1): 
            return maps[limitRow-1][limitCol-1]
        for i in range(4):
            if 0 <= tmpX + dx[i] < limitRow and 0 <= tmpY + dy[i] < limitCol and maps[tmpX + dx[i]][tmpY + dy[i]] == 1: 
                if  not visited[tmpX + dx[i]][tmpY + dy[i]]:
                    maps[tmpX + dx[i]][tmpY + dy[i]] = maps[tmpX][tmpY]+1
                    queue.append((tmpX + dx[i],tmpY + dy[i]))
                    visited[tmpX + dx[i]][tmpY + dy[i]] = True
    return -1

def solution(maps):
    # 행과 열을 안받았음..
    queue = deque([(0,0)])
    limitCol = len(maps[0])
    limitRow = len(maps)
    visited = [[False]*limitCol for _ in range(limitRow)]
    answer = BFS(queue,maps,limitCol,limitRow,visited)
    print(answer)
    return answer