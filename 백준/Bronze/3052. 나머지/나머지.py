dict = {}
cnt = 0
for i in range(10):
    n = int(input())
    m = n % 42
    if m in dict:
        continue
    else:
        dict[m] = 1
        cnt += 1
print(cnt)
      