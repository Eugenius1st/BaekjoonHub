import sys

from itertools import permutations
arr = []
a,b = map(int,input().split())

for i in range(1,a+1):
    arr.append(i)

arr = list(permutations(arr, b))

for i in arr:
    for x in i:
        print(x,end=" ")
    print()
