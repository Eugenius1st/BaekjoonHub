import sys

def input():
    return sys.stdin.readline().rstrip()

A,B,C = map(int,input().split())

if(C-B<=0): print(-1)
else:
    val = A//(C-B)
    if (A%(C-B)>=0): val+=1
    print(val)
