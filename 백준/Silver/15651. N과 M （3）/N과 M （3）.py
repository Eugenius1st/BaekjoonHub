import sys
#sys.stdin=open("input.txt", "rt")

M, N = map(int,input().split())
s = []

def dfs():
    if len(s)==N :
        print(' '.join(map(str,s)))
        return 
    for i in range(1,M+1):
        s.append(i)
        dfs()
        s.pop()
dfs()