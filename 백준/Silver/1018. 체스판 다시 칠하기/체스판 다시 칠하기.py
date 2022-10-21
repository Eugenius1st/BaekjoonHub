import sys

N,M = map(int,input().split())
cnt1 = 0
cnt2 = 0
chess_board = [] 
ch = ["B","W"]
minimum = 2147000000

for _ in range(N):
    chess_board.append(input())


# 전체를 돈다
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0

        # 전체 돌면서 기준점+8까지 또 돈다
        for x in range(i,i+8):
            for y in range(j,j+8):

                if(y%2==0):
                    # y가 짝수
                    if (x%2==0 and chess_board[x][y] != ch[0]) : cnt1 +=1
                    elif (x%2==1 and chess_board[x][y] != ch[1]): cnt1 +=1
                    if (x%2==0 and chess_board[x][y] != ch[1]) : cnt2 +=1
                    elif (x%2==1 and chess_board[x][y] != ch[0]): cnt2 +=1

                    #print(cnt1,cnt2)
                else:
                    if (x%2==0 and chess_board[x][y] != ch[1]) : cnt1 +=1
                    elif (x%2==1 and chess_board[x][y] != ch[0]): cnt1 +=1
                    if (x%2==0 and chess_board[x][y] != ch[0]) : cnt2 +=1
                    elif (x%2==1 and chess_board[x][y] != ch[1]): cnt2 +=1
                    
        #print(cnt2)
        if minimum > min(cnt1,cnt2): minimum = min(cnt1,cnt2)
        #print(minimum)

print(minimum)
