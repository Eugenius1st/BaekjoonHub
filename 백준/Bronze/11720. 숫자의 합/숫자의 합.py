n = int(input())
std = int(input())
res = 0
for i in range(n):
    res += std % 10
    std //= 10
print(res)