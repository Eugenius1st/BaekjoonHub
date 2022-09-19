import sys
N = int(input())
arr = []
for i in range(N):
    tmp = int(input())
    arr.pop() if tmp == 0 else arr.append(tmp)        
print(sum(arr))