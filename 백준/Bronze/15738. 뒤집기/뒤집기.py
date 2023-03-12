# A 크기 K 위치 M 연산의 개수 / 배열 / 연산들(+1 된 상태)
A, K, M = map(int, input().split())
arr = list(map(int,input().split()))
currentPos = K
# print(currentPos)
for i in range(M):
    calculate = int(input())
    if calculate > 0 and currentPos <= calculate:
        currentPos = abs(currentPos - (calculate + 1))
        # print("here1", currentPos)
    elif calculate < 0 and currentPos > calculate+A:
        currentPos = abs(A - currentPos + 1 + (A+calculate))
        # print("here2",currentPos)
    else:
        # print("here4", currentPos)
        continue
print(currentPos)