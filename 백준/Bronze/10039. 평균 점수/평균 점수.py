import sys
#sys.stdin = open("input.txt", "rt")

arr = []
for i in range(5):
    tmp = int(input())
    if tmp < 40: arr.append(40)
    else: arr.append(tmp)

res = sum(arr)

print(res//5)