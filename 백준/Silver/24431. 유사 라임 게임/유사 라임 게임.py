if __name__ == '__main__':
    # L 개수 F 단어 길이 M 반복 개수
    # dictionary 만들어서  count + 한다. 이후 2개 이상인 것이 단어에 들어 있는지 확인
    A = int(input())

    for i in range(A):
        dict = {}
        res = 0
        L, F, M = map(int, input().split())
        arr = list(input().split())
        for j in arr:
            tmpStr = j[-M:]
            if tmpStr in dict:
                dict[tmpStr] += 1
            else:
                dict[tmpStr] = 1
        for j in dict:
            if dict[j] > 1:
                res += dict[j] // 2
        print(res)