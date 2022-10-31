import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**8)

def input():
    return sys.stdin.readline().rstrip()

N,M,start = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer = [0] * (N+1)
dq = deque()
cnt = 1 # 방문 순서 카운팅

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬!! 이걸 안해서 틀렸넹
for i in graph:
    i.sort()

def dfs(visited, graph, start):
    global cnt
    visited[start] = 1
    answer[start]=cnt
    dq.append(start)
    while(dq):
        tmp = dq.popleft()       
        for i in graph[tmp]:
            if visited[i]==1: continue            
            else:
                cnt+=1
                answer[i]=cnt
                visited[i] = 1
                dq.append(i)
            
           
dfs(visited, graph, start)
for i in range(1,N+1):
    print(answer[i])

#bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#    for each v ∈ V - {R}
#        visited[v] <- NO;
#    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#    while (Q ≠ ∅) {
#        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#            if (visited[v] = NO) then {
#                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#            }
#    }
#}