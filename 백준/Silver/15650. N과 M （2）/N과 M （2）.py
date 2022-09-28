import sys
#sys.stdin=open("input.txt", "rt")

M, N = map(int,input().split())
s = []

def dfs(st):
    if len(s)==N :
        print(' '.join(map(str,s)))
        return 
    for i in range(st,M+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)