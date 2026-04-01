def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = True
    for i in phone_book:
        tmp = ""
        if i in dic :
            continue
        for j in i:
            tmp += j
            if tmp in dic:
                print(tmp)
                return True
            