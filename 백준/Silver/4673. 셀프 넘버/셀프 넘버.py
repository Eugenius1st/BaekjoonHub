# 10000보다 작거나 같은 셀프 넘버
N = 10001
arr = [0]*N

for i in range(1, N):
    tmp = 0
    k = i
    tmp += i
    while i > 0:
        tmp += i % 10
        i //= 10
    if tmp >= N:
        continue

    arr[tmp] = k

for i in range(1, N):
    if arr[i] == 0:
        print(i)