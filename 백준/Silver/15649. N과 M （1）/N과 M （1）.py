import sys
from itertools import permutations
arr = []
a,b = map(int,input().split())

arr = list(permutations(range(1,a+1), b))

for i in arr:
    res = " ".join(map(str,i))
    print(res)
