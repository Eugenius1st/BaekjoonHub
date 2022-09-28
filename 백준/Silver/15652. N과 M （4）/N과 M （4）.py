import sys
#sys.stdin=open("input.txt", "rt")

M,N = map(int,input().split())
s = []
def dfs(start):
    if(len(s) == N):
        print(' '.join(map(str,s)))
        return
    for i in range(start,M+1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)