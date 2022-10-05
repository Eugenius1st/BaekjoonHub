import sys
from collections import deque

# 큐를 이용할 것이다.
# while 문의 array값이 false가 될 때까지
# pop 과 append 반복하다가 k 번째에
# 새로운 배열에 append 시킬 것이다

n, k = map(int,input().split())
cnt = 0

dQ = list(range(1,n+1))
dQ = deque(dQ)
res = []

while dQ:
    cnt+=1
    tmp = dQ.popleft()
    if cnt==k:
        res.append(tmp)
        cnt = 0
    else:        
        dQ.append(tmp)
        

print('<' + ', '.join(map(str, res)) + '>')
#join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수입니다.
# '구분자'.join(리스트)







