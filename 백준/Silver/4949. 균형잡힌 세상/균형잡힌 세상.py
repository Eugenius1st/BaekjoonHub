import sys


def input():
    return sys.stdin.readline().rstrip()

def checkText(text):
    ch = []
    tmp = ""
    for i in text:
        if i == "(": ch.append("(")
        elif i == ")":
            if(len(ch)==0): return "no"
            tmp = ch.pop()
            if(tmp=="["):return "no"

        if i == "[": ch.append("[")
        elif i == "]":
            if(len(ch)==0): return "no"
            tmp = ch.pop()
            if(tmp=="("):return "no"
        else: continue
    if(len(ch)==0): return "yes"
    else: return "no"

if __name__ == "__main__":
    text=""  
    while(True):
        text = input()
        if (text=="."):break
        print(checkText(text))