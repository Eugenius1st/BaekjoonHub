import sys

def input():
    return sys.stdin.readline().rstrip()


chess = [1,1,2,2,2,8]
arr = list(map(int,input().split()))
for x in range(len(chess)):
    arr[x] = chess[x] - arr[x]
print(" ".join(str(_)for _ in arr))

# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8