import sys


N = int(input())
line = list(map(int,input().split()))
acc = 0
answer = 0

line.sort()

for x in line:
    acc += x
    answer += acc
print(answer)