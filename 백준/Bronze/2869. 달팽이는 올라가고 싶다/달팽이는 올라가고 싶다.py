A, B, V = map(int,input().split())

N = A - B
V -= A
cnt = 1

res = V // N
tmp = V % N

cnt += res

if tmp > 0:
    cnt += 1
print(cnt)