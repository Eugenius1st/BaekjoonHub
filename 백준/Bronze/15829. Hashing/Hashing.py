import sys

# r은 31
N = int(input())
line = input()
res = 0

for i in range(N):
    res += (ord(line[i])-96 )* (31**i)
print(res% 1234567891)
