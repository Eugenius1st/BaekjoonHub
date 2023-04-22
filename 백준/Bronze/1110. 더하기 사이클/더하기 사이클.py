import sys


N = int(input())
cnt = 0
newN = N
while True:
    a, b = newN // 10, newN % 10
    res = a + b # 2 + 6 = 8

    x = b * 10
    y = res % 10
    newN = x+y
    cnt += 1
    if newN == N:
        break

print(cnt)