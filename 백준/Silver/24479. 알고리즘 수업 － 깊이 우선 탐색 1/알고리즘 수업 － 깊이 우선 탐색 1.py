import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 6)  
# sys.stdin=open("input.txt", "rt")
# 정점 수, 간선 수, 시작 정점

N, M, R = map(int,input().split())

# 연결 노드 그래프 초기화(1번 노드와 인덱스 값이 같게 하기 위해 n+1)
# [[],[],[],[],[],[]]
graph = [[]for _ in range(N+1)]

# 방문 순서 그래프(이것도 인덱스 값과 노드의 값이 동일하게 만들기 위해서 n+1)
visited = [0]*(N+1)

# 순차 입력
cnt = 1

for i in range(M): #연결된 노드 입력받기
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):# 오름차순 정리
    graph[i].sort()

def dfs(graph, v, visited):
    global cnt

    # 연결된 노드 방문
    visited[v]=cnt
    for i in graph[v]:
        if visited[i]==0: # 방문 안한 노드일경우
            cnt += 1
            dfs(graph, i, visited) # dfs 실행

dfs(graph,R,visited)

# 출력하기
for i in range(1,N+1):
    print(visited[i])