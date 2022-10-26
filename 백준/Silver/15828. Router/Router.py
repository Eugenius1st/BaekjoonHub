import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
packet = 0
router_buffer = deque([0 for _ in range(packet)])
bufferLen = int(input())

while(packet != -1):
    packet = int(input())
    if packet == -1 : break
    if packet == 0:
        router_buffer.popleft()
    else:
        if len(router_buffer) >= bufferLen:continue
        router_buffer.append(packet)

print("\n".join(map(str, router_buffer)) if router_buffer else "empty")    
