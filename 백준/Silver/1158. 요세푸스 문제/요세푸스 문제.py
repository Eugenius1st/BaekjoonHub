import sys
# BOJ__1158__덱
from collections import deque
N,K = map(int,input().split())
arr= deque(list(range(1,N+1)))
cnt = 0
res = []
while arr:
    tmp = arr.popleft()
    cnt+=1
    if cnt == K:
        cnt = 0
        res.append(tmp)
    else:
        arr.append(tmp)
print("<"+", ".join(map(str,res))+">")