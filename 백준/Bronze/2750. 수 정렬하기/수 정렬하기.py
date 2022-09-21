import sys
#from collections import deque
# sys.stdin=open("input.txt", "rt")
arr = []
n = int(input())
# 버블정렬
for i in range(n):
    tmp=int(input())
    arr.append(tmp)

for i in range(n):
    swap = "";
    for j in range(0,n-1-i):
        if(arr[j]>arr[j+1]):
            swap = arr[j]
            arr[j] = arr[j+1] 
            arr[j+1] = swap
    if swap =="": break

for x in arr:
    print(x)