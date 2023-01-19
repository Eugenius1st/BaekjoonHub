H,M = map(int,input().split())
time = int(input())
M += time

while M >= 60:
    M -= 60
    H += 1
if H >= 24:
    H -= 24

print(H,M)