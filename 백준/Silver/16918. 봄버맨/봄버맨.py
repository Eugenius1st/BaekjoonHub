from collections import deque
import sys

# 1. checkBomb, queue에 담음
# 2. 폭탄 설치 plantBomb
# 2. queue 폭탄 폭파 상우좌하 폭탄 폭발 & checkBomb queue에 담음
def BFS():
    while queue:
        y, x = queue.popleft()
        board[y][x] = '.'
        if 0 <= y - 1:
            board[y - 1][x] = '.'
        if 0 <= x - 1:
            board[y][x - 1] = '.'
        if y + 1 < N:
            board[y + 1][x] = '.'
        if x + 1 < M:
            board[y][x + 1] = '.'

def checkBomb(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == "O":
                queue.append((i, j))

def plantBomb(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == '.':
                board[i][j] = 'O'

if __name__ == "__main__":
    N, M, K = map(int,input().split())
    board = []
    for i in range(N):
        board.append(list(sys.stdin.readline().rstrip()))
        # string 은 끝에 \n있어서 rstrip로 읽어준다
    K -= 1
    while K:
        queue = deque()
        checkBomb(board)
        plantBomb(board)
        K -= 1
        if K == 0:
            break
        BFS()
        K -= 1
    for i in range(N):
        for j in range(M):
            print(board[i][j], end="")
        print()