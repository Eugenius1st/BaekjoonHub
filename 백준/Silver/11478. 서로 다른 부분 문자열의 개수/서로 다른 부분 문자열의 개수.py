import sys
#sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

def chText(txt,idx,N):
    for i in range(idx+1,N+1):
        tmp=txt[idx:i]
        if tmp in dic:continue
        else: dic[tmp] = 1


if __name__ == "__main__":
    dic = dict()
    text = input()
    for i in range(len(text)):
        chText(text,i,len(text))

    print(len(dic))

