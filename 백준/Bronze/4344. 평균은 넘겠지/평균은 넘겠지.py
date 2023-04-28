from collections import deque
import sys

#소수점 셋째 자리까지 출력
N = int(input())
for i in range(N):
    arr = list(map(int,input().split()))
    avgN = sum(arr[1:])/arr[0]
    cnt = 0
    for j in range(1,arr[0]+1):
        if arr[j] > avgN:
            cnt += 1
    if cnt == 0:
        res = 0
    else:
        res = (cnt/arr[0])*100
    print(f'{res:.3f}%')