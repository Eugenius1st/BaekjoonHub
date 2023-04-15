from collections import deque
import sys


re = int(input())

for _ in range(re):
    # 문서의 개수 N, 몇번째에 놓였는지 M(0부터)
    N, M = map(int, input().split())
    # 중요도
    arr = list(map(int,input().split()))
    deqArr = deque([])
    for i in range(len(arr)):
        if i == M:
            deqArr.append((arr[i], True))
        else:
            deqArr.append((arr[i], False))
    maxN = max(arr)
    cnt = 0
    while True:
        if deqArr[0][0] < maxN:
            deqArr.append(deqArr.popleft())
        else:
            ch = deqArr.popleft()
            if deqArr:
                maxN = (max(deqArr)[0])
            cnt += 1
            if ch[1]:
                break
    print(cnt)