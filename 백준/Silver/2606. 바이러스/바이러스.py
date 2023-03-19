import sys

input = sys.stdin.readline
    # 방문하지 않은 노드라면 재귀 호출

n = int(input())
m = int(input())
# 정점, 연결 수
graph = [[] for _ in range(n+1)]
visitedG = []

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

def DFS(graph, curNode, visited ): # 인자로 그래프, 현재노드, 방문그래프
    visited.append(curNode)
    graph[curNode].sort()
    # 현재 노드와 인접한 노드 확인
    for linkNode in graph[curNode]:

        if linkNode not in visited:
            DFS(graph, linkNode, visited)
DFS(graph, 1, visitedG)
print(len(visitedG)-1)
