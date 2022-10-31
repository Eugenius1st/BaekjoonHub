import sys
#sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10 ** 8)

def input():
    return sys.stdin.readline().rstrip()


def dfs(visited,graph,start):
    global cnt
    visited[start] = 1
    answer[start]=cnt
 #   print(start)
    for i in graph[start]:
        if(visited[i]==0):
            cnt+=1
            dfs(visited,graph,i)

N,M,start = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer = [0] * (N+1)
cnt = 1

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse = True)

dfs(visited,graph,start)
for i in range(1,N+1):
    print(answer[i])

#dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
#        if (visited[x] = NO) then dfs(V, E, x);}