import sys

def input():
    return sys.stdin.readline().rstrip()


A = int(input())
B = int(input())
val = 0
cnt = 1
while(B>0):
    tmp = B%10
    B //= 10
    print(A*tmp)
    val+= A*tmp*(cnt)
    cnt*=10
print(val)