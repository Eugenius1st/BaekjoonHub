import sys
#sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()


def cutPaper(x,y,N):
    global cnt0, cnt1

    ch = paper[x][y]
    for curX in range(x,x+N):
        for curY in range(y,y+N):
            if ch != paper[curX][curY]:
                cutPaper(x,y,N//2)
                cutPaper(x+N//2,y,N//2)
                cutPaper(x,y+N//2,N//2)
                cutPaper(x+N//2,y+N//2,N//2)
                return
    if ch == 0 : 
        cnt0 += 1
    else: 
        cnt1 += 1


if __name__ == "__main__":
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    cnt0 = 0
    cnt1 = 0

    cutPaper(0,0,N)
    print(cnt0,cnt1)