def solution(s):
    ch = []
    for x in s:
        if x == "(":
            ch.append("(")
        elif x == ")":
            if len(ch)==0: return False
            ch.pop()    
    if len(ch)!=0: return  False
    return True