arr = []
for i in range(1,10):
    n = int(input())
    arr.append((n,i))
maxN = max(arr)

print(maxN[0])
print(maxN[1])