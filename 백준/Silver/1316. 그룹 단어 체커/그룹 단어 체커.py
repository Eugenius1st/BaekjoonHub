
# arr = list(map(int,input().split()))
# for i in arr:
#     res += i**2
cnt = int(input())
res = 0
lastAlpha = ""
for i in range(cnt):
    arr = []
    text = str(input())
    for j in text:
        if j in arr and j == lastAlpha:
            continue
        elif j in arr and j != lastAlpha:
            break
        elif j not in arr:
            lastAlpha = j
            arr.append(j)
    else:
        res += 1
print(res)