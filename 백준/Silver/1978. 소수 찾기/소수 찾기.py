import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int,input().split()))
cnt = 0

for x in arr:
    if x == 1:
        continue
    if x == 2:
        cnt +=1
        continue
    else:
        for i in range(2, x-1):
            if x%i == 0:
                break
        else: 
            cnt+=1
print(cnt)