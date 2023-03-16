from collections import deque
import sys
#sys.stdin = open("input.txt", "rt")
# 1은 좌 우 반대로 = x좌표 * (-1)
# 2는 상 하 반대로 = y좌표 * (-1)
# 3은 우에서 상으로, 하에서 좌로 / 좌에서 하로, 상에서 우로 = 좌표 변경 후 * (-1)
# 4는 우로에서 하로, 하에서 우로 / 좌에서 상으로, 상에서 좌로 = 좌표 변경
# recursion error 나니까 BFS 로 바꿔야 될 것 같다!
def BFS(haveToGo, visited, arr, curCase, row, col):
    while haveToGo:
        curPos = haveToGo.popleft()
        case = curCase.popleft()
        curY = curPos[0] + case[0]
        curX = curPos[1] + case[1]
        # print(curPos)
        # print(curPos,case)
        if row > curY >= 0 and col > curX >= 0:
            visited[curY][curX] = 1
            nextPos = (curY, curX)
            if arr[curY][curX] == 9:
                break
            if arr[curY][curX] == 1:
                visited[curY][curX] = 1
                # 좌우로(0,1) (0,-1) 오는 경우 종료, 상하는 진행
                if case == (1,0) or case == (-1, 0):
                    haveToGo.append(nextPos)
                    curCase.append(case)
                else:
                    break
            elif arr[curY][curX] == 2:
                visited[curY][curX] = 1
                # 상하로 오는 경우 종료, 좌우는 진행
                if case == (0,1) or case == (0, -1):
                    haveToGo.append(nextPos)
                    curCase.append(case)
                else:
                    break
            elif arr[curY][curX] == 3:   # "up","right" 으로 온 경우 / "down","left" 으로 온 경우 중복처리
                if "ur3" not in str(visited[curY][curX]) and (case == (-1, 0) or case == (0, 1)):
                    visited[curY][curX] = str(visited[curY][curX])+"ur3"
                    tmpCase = (case[1]*(-1), case[0]*(-1))
                    haveToGo.append(nextPos)
                    curCase.append(tmpCase)
                elif "dl3" not in str(visited[curY][curX]) and (case == (1, 0) or case == (0, -1)):
                    visited[curY][curX] = str(visited[curY][curX])+"dl3"
                    tmpCase = (case[1]*(-1), case[0]*(-1))
                    haveToGo.append(nextPos)
                    curCase.append(tmpCase)
                else:
                    break
            elif arr[curY][curX] == 4:   # "up","left" 으로 온 경우 / "down","right" 으로 온 경우 중복처리
                # visited[curY][curX] = 1
                # tmpCase = (case[1], case[0])
                # haveToGo.append(nextPos)
                # curCase.append(tmpCase)
                if "ul4" not in str(visited[curY][curX]) and (case == (-1, 0) or case == (0, -1)):
                    visited[curY][curX] = str(visited[curY][curX])+"ul4"
                    tmpCase = (case[1], case[0])
                    haveToGo.append(nextPos)
                    curCase.append(tmpCase)
                elif "dr4" not in str(visited[curY][curX]) and (case == (1, 0) or case == (0, 1)):
                    visited[curY][curX] = str(visited[curY][curX])+"dr4"
                    tmpCase = (case[1], case[0])
                    haveToGo.append(nextPos)
                    curCase.append(tmpCase)
                else:
                    break
            else:
                haveToGo.append(nextPos)
                curCase.append(case)

if __name__ == '__main__':
    row, col = map(int, input().split())
    arr = []
    std = []
    visited = list([0] * col for _ in range(row))
    # 이차원 배열 담기
    for i in range(row):
        arr.append(list(map(int, input().split())))
    # 에어컨이 있는 위치(9) 찾기
    for i in range(row):
        for j in range(col):
            if arr[i][j]== 9:
                std.append((i,j))
    # 에어컨 개수 만큼 BFS 반복 호출
    case = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if len(std) == 0:
        print(0)
    else:
        for i in range(len(std)):
            visited[std[i][0]][std[i][1]] = 1
            for j in range(4):
                haveToGo = deque([std[i]])
                curCase = deque([case[j]])
                # print(haveToGo, curCase)
                BFS(haveToGo, visited, arr, curCase, row, col)
            cnt = 0
        for i in range(row):
            # print(visited[i])
            for j in range(col):
                if visited[i][j] != 0:
                    cnt += 1
        print(cnt)



