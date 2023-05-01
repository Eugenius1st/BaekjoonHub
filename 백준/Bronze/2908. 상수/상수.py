A, B = map(int,input().split())
n = 0
m = 0
while A > 0:
    n *= 10
    n += A %10
    A = A//10
while B > 0:
    m *= 10
    m += B%10
    B = B//10

print(max(n,m))