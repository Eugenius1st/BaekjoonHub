import sys
import math

def input():
    return sys.stdin.readline().rstrip()

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    res = 0

    res = math.factorial(m) // (math.factorial(m-n)*math.factorial(n))
    print(res)

