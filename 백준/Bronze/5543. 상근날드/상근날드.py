answer = -50
buger = 2147000000
drink = 0
for i in range(3):
    n = int(input())
    buger = min(n, buger)
cok = int(input())
cy = int(input())
answer += min(cok, cy)
answer += buger
print(answer)