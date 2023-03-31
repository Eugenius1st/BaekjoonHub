N = int(input())
arr = list(map(int,input().split()))
M = int(input())
res = 0
for i in arr:
    if i == M: res+=1
print(res)