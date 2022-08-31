def solution(n): #자바스크립트에서 내가 짠거랑 똑같이 적었는데 되더라..... 걍 MAX int 문제인걸로
    num = n
    answer = 0
    remainN = 0
    tmpN = ''
    multiN = 0
    while num > 0 :
        remainN = num %3
        num = num // 3
        tmpN += str(remainN)

    num = int(tmpN)

    while num > 0:
        remainN = num % 10
        num = num // 10
        answer += remainN * (3**multiN)
        multiN+=1

    return answer