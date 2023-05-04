# 1 7 19 37
#  +6 +12 +18
N = int(input())
tmp = 1
std = 6
M = 6
cnt = 1

while N > tmp:
    tmp += std
    std += M
    cnt += 1
print(cnt)