import sys

N = int(input())
cnt = 1
standard = 666
while(cnt<N):
    standard += 1
    if "666" in str(standard):
        cnt += 1
    
print(standard)