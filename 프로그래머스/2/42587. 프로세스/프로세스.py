from collections import deque 
# 중요도가 높은 문서를 먼저 인쇄    
def solution(priorities, location):
    idxs = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)
    ans = []
    
    cnt = 0
    while priorities:
        tmp = priorities.popleft()
        idxTmp = idxs.popleft()
        
        maxTmp = max(priorities) if len(priorities) > 0 else 0  # 항상 마지막 요소를 고려하면서 생각해! 배열이 비어있을 수도있고. 이부분에서 자주 헷갈리는 듯
        if maxTmp <= tmp:
            cnt += 1
            if idxTmp == location:
                return cnt
        else: 
            priorities.append(tmp)
            idxs.append(idxTmp)
            
    return
