from collections import deque
import sys

# 모든 지점으로 부터 목표 지점까지의 거리 구하기
def BFS(destination):
    queue = deque([destination])
    while queue:
        pos = queue.popleft()
        # 상
        if pos[0] - 1 >= 0 and board[pos[0] - 1][pos[1]] == 1 and not visited[pos[0] - 1][pos[1]]:
            board[pos[0] - 1][pos[1]] = board[pos[0]][pos[1]] + 1
            queue.append((pos[0] - 1, pos[1]))
            visited[pos[0] - 1][pos[1]] = True
        # 하
        if pos[0] + 1 < N and board[pos[0] + 1][pos[1]] == 1 and not visited[pos[0] + 1][pos[1]]:
            board[pos[0] + 1][pos[1]] = board[pos[0]][pos[1]] + 1
            queue.append((pos[0] + 1, pos[1]))
            visited[pos[0] + 1][pos[1]] = True
        # 좌
        if pos[1] - 1 >= 0 and board[pos[0]][pos[1] -1] == 1 and not visited[pos[0]][pos[1] - 1]:
            board[pos[0]][pos[1] - 1] = board[pos[0]][pos[1]] + 1
            queue.append((pos[0], pos[1] - 1))
            visited[pos[0]][pos[1] - 1] = True
        # 우
        if pos[1] + 1 < M and board[pos[0]][pos[1] + 1] == 1 and not visited[pos[0]][pos[1] + 1]:
            board[pos[0]][pos[1] + 1] = board[pos[0]][pos[1]] + 1
            queue.append((pos[0], pos[1] + 1))
            visited[pos[0]][pos[1] + 1] = True

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    visited = []
    destination = (0, 0)
    # 땅 초기화
    for i in range(N):
        board.append(list(map(int,input().split())))
        visited.append([False]*M)
    # 목적지 초기화
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                board[i][j] = 0
                visited[i][j] = True
                destination = (i, j)
    BFS(destination)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                board[i][j] = -1
    for i in board:
        print(*i)
