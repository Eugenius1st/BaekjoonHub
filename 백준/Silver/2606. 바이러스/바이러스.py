def DFS(visited, node, cnt):
    if not visited[node]:
        visited[node] = 1
        for i in arr[node]:
            DFS(visited, i, cnt+1)

if __name__ == "__main__":
    N = int(input()) # 노드 개수
    M = int(input()) # 간선 개수
    arr = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(M):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    DFS(visited, 1, 1)
    print(sum(visited)-1)