import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    q=deque()
    q.append(1)
    while q:
        node = q.pop()
        for i in graph[node]:
            if parent[i]==0:
                parent[i]=node
                q.append(i)
    return parent

bfs()

for i in parent[2:]:
    print(i)

