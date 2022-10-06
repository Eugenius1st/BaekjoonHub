import sys
from collections import deque

n = int(input())
arr = deque(list(range(1,n+1)))
tmp = 0

while len(arr)>1:
    print(arr.popleft(),end=" ") 
    tmp = arr.popleft()
    arr.append(tmp)
print(arr.popleft()) #여기네..
