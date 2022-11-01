import sys
from collections import deque

sys.setrecursionlimit(10**8)

def input():
    return sys.stdin.readline().rstrip()

initial, row, col = map(int,input().split())
text = list(input())
answer = ""

for i in range(1,row):
    tmp = input()
    for j in range(initial*col):
        if text[j] == '?' and tmp[j] !='?':
            text[j] =tmp[j]
for i in range(0,initial*col,col):
    for j in range(col):
        if text[i+j] != '?':
            answer += text[i+j]
            break
    else:
        answer += '?'
print(answer)