import sys


s = input()
stack = []

# 괄호 배열이 올바른지 확인하는 로직
for x in s:
    if x =='(':
        stack.append('(')

    elif x == '[':
        stack.append('[')

    elif stack and x ==')':
        if stack[-1] == '(':
            stack.pop()
    elif stack and x == ']':
        if stack[-1] == '[':
            stack.pop()
    else:
        print(0)
        exit()
if stack:
    print(0)
    exit()

# 올바른 괄호 배열을 계산하는 로직

def plus():
    while len(stack)>1: # 무조건 0보다는 커야 한다
        a, int1 = stack[-1]
        b, int2 = stack[-2]
        if a or b:
            break
        stack.pop()
        stack.pop()
        stack.append((None, int1+int2))

for x in s:
    if x == '(':
        stack.append(('(',2))
    elif x == '[':
        stack.append(('[',3))
    elif x == ')' or x == ']':
        lastB, lastN = stack.pop()
        if lastB != None: # 괄호가 있는 경우
            stack.append((None, lastN)) # 숫자로 바꾸어 stack에 쌓는다
        else: # 괄호가 없고 직전이 숫자인 경우 곱하기 해 주어야 한다
            a , b = stack.pop()
            stack.append((None, lastN * b))
        plus()
print(stack[-1][1])

    