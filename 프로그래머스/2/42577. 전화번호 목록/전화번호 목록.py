def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = True
    for i in phone_book:
        tmp = ""
        for j in range(len(i)-1):
            tmp += i[j]
            if tmp in dic:
                print(tmp)
                return False
    else:
        return True
            