arr = list(map(int,input().split()))
res = 0
for i in arr:
    res += i**2
print(res%10)