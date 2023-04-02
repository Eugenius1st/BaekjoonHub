from collections import deque
import sys

dy = [-1,0,1,0]
dx = [0,-1,0,1]
def BFS(matureTomato):
    matureTomato = deque(matureTomato)
    while matureTomato:
        tomato = matureTomato.popleft()
        for i in range(4):
            if 0 <= tomato[0]+dy[i] < N and 0 <= tomato[1]+dx[i] < M and box[tomato[0]+dy[i]][tomato[1]+dx[i]] != -1:
                if box[tomato[0]+dy[i]][tomato[1]+dx[i]] == 0:
                    box[tomato[0] + dy[i]][tomato[1] + dx[i]] = box[tomato[0]][tomato[1]] + 1
                    matureTomato.append((tomato[0] + dy[i], tomato[1] + dx[i]))
                elif box[tomato[0]+dy[i]][tomato[1]+dx[i]] > box[tomato[0]][tomato[1]] + 1:
                    box[tomato[0] + dy[i]][tomato[1] + dx[i]] = box[tomato[0]][tomato[1]] + 1
                    matureTomato.append((tomato[0] + dy[i], tomato[1] + dx[i]))
if __name__ == "__main__":
    # M 세로 N 가로
    M, N = map(int, input().split())
    box = []
    matureTomato = []
    checkZero = [0] * (N)
    checkStart = [0] * (N)
    # 토마토가 하나 이상 있는 경우만 입력으로 주어진다
    for i in range(N):
        box.append(list(map(int,input().split())))
        if 0 in box[i]:
            checkZero[i] = 1
        if 1 in box[i]:
            checkStart[i] = 1

    # 1이 없는 경우, 즉 시작 토마토가 없는 경우
    if sum(checkStart) == 0:
        print(-1)
        exit(0)
    # 시작부터 토마도 박스에 익어야할 토마토가 없는 경우
    if sum(checkZero) == 0:
        print(0)
        exit(0)

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                matureTomato.append((i,j))
    # print(matureTomato)
    # 토마토 박스가 모두 익은 경우 return 최소 날짜
    BFS(matureTomato)
    result = 0
    for i in range(N):
        result = max(result,max(box[i]))
        # 토마토 박스에 0이 있는 경우 -1
        for j in range(M):
            if box[i][j] == 0:
                print(-1)
                exit(0)
    print(result-1)

