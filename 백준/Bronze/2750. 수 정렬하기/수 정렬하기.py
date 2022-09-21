import sys
#from collections import deque
#sys.stdin=open("input.txt", "rt")
arr = []
n = int(input())
# 삽입정렬
for i in range(n):
    tmp=int(input())
    arr.append(tmp)

for end in range(1,n):
    i = end
    while i > 0 and arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        i -= 1
    
for x in arr:
    print(x)
    
# 삽입정렬
   