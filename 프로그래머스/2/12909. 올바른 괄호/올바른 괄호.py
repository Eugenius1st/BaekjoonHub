from collections import deque

def solution(s):
    open = []
    data = deque(s)
    while data:
        tmp = data.popleft()
        if(tmp == "("):
            open.append(tmp)
        else:
            if(len(open)>0):
                open.pop()
            else: return False
    else: 
        if(len(open)) > 0: return False
    return True 