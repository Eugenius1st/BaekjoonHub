import sys
import heapq as hq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
result = []

for i in range(N):
    num = int(input())
    if num == 0:
        if len(result)==0:
            print(0)
        else:
            # heappop하면 인덱스0번째 값으로 비교하지만
            # 같은 크기의 값일시 에러남 따라서
            res = hq.heappop(result)[1]
            # 같은크기의 값의 인덱스1번째 값으로 비교하여 pop하도록 함
            print(res)

    else:
        hq.heappush(result, [abs(num), num])
        # push에 배열로 전달 가능
        # 절댓값 함수써서 인자 넣는다
