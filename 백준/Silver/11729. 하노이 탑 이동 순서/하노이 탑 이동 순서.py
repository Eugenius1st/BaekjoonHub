import sys
#from collections import deque
#sys.stdin=open("input.txt", "rt")

def hanoi(n,fromN,subN,toN):
    global cnt
    if n==0 :return
    hanoi(n-1,fromN,toN,subN)
    cnt+=1
    answer.append([fromN,toN])
    hanoi(n-1,subN,fromN,toN)


n = int(input())
answer = [];
cnt = 0
hanoi(n,1,2,3)
print(cnt)
for x in answer:
    print(x[0],x[1])
   