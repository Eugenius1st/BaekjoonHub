import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []

for i in range(N):
    s, e = map(int,input().split())
    arr.append((s,e))

# 튜플로 저장해서 끝나는 시간을 기준으로 정렬한다
# 회의가 끝나는 시간과 가장 가까운 다음 회의 시작 시간을 기준으로 새로운 회의가 진행되도록 한다.

# 두번째 원소로 정렬하는 방법 >> 람다 함수 사용!!
# arr.sort(key=lambda x:x[1])
# + 첫번째 원소로 '내림차순'정렬하는 방법 >> arr.sort(key=lambda x:x[0], reverse=True)
#arr.sort(key = lambda x:x[1])
#근데 위가 에러나서 아래로 고쳐주었다
arr.sort(key = lambda x : (x[1],x[0]))
# 이것이 의미하는 것은 x[1]기준으로 오름차순 정렬하고 x[1]값이 같다면 x[0]을 기준으로 정렬한다는 뜻이다.
# 조금더 섬세함 ㅇㅇ
cnt = 1
std = arr[0][1]

for j in range(1,N):
    if std <= arr[j][0]:
        std = arr[j][1]
        cnt += 1
print(cnt)