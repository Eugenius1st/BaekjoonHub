#10845
import sys
from collections import deque
#sys.stdin=open("input.txt", "rt")
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
queue = deque()

for x in range(N):
    tmp = input()
    if "push" in tmp:
        tmp = tmp.split(" ")
        queue.append(tmp[1])
    elif "pop" in tmp:
        if len(queue) == 0: print(-1)
        else:
            tmp = queue.popleft()
            print(tmp)
    elif "size" in tmp:
        print(len(queue))
    elif "empty" in tmp:
        if len(queue) == 0: print(1)
        else: print(0)
    elif "front" in tmp:
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    else:
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue)-1])