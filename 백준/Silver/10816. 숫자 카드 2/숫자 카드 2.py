import sys


N = int(input())
tmp = list(map(int,input().split()))
my_card=dict()
for x in tmp:
    if x not in my_card: my_card[x] = 1
    else: my_card[x]+=1

M = int(input())
standard_card = list(map(int,input().split()))
res = [0]*M

for x in range(M):
    if standard_card[x] in my_card:
        res[x]=my_card[standard_card[x]]

print(*res)