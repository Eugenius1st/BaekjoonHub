#11047번 동전
import sys
#sys.stdin=open("input.txt", "rt")
N,K = map(int,input().split())
coins = []
answer = 0

for x in range(N):
    tmp = int(input())
    coins.append(tmp)


for i in range(N-1,-1,-1):
    answer += K//coins[i]
    K %= coins[i]

print(answer)

