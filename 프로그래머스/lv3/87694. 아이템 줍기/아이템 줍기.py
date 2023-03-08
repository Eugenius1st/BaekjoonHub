from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(positions,haveToGo,itemPos,maxX,maxY):
    while haveToGo:    
        currentPos = haveToGo.popleft()
        currentX = currentPos[1]
        currentY = currentPos[0]

        if currentX == itemPos[1] and currentY == itemPos[0]:
            print((positions[currentY][currentX]/2)-0.5)
            return ((positions[currentY][currentX]/2)-0.5)
        for i in range(4):
            if 0 < currentX + dx[i] < maxX and 0 < currentY + dy[i] < maxY :
                #print(currentX + dx[i],currentY + dy[i])
                if positions[currentY + dy[i]][currentX + dx[i]] == 1 or positions[currentY + dy[i]][currentX + dx[i]] >= positions[currentY][currentX]+1: 
                    haveToGo.append((currentY + dy[i],currentX + dx[i]))
                    positions[currentY + dy[i]][currentX + dx[i]] = positions[currentY][currentX]+1
        #for k in range(len(positions)):
        #    print(positions[k])
    return 0

        

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 즉 1,1 1,4 7,1 7,4
    answer = 0
    maxX = 0
    maxY = 0
    for i in range(len(rectangle)):
        maxX = max(maxX,rectangle[i][0],rectangle[i][2])
        maxY = max(maxY,rectangle[i][1],rectangle[i][3])
    # 겹쳐서 구별할 수 없는 경우 때문에 2 배로 늘려서 배열을 만든다!
    maxX = maxX*2 
    maxY = maxY*2 
    positions = [[-1]*(maxX) for _ in range(maxY)]

    for i in rectangle:
    
        for j in range(i[0]*2-1,i[2]*2): # X
            for k in range(i[1]*2-1,i[3]*2): # Y
                if (positions[k][j]==-1 or positions[k][j]==1) and(j == i[0]*2-1 or j == i[2]*2-1 or k == i[1]*2-1 or k == i[3]*2-1): positions[k][j] = 1 
                else: positions[k][j] = 0


    characterPos = (characterY*2-1,characterX*2-1)
    itemPos = ( itemY*2-1,itemX*2-1)
    haveToGo = deque([characterPos])
    answer = BFS(positions,haveToGo,itemPos,maxX,maxY)

    return answer