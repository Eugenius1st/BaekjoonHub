import sys

def input():
    return sys.stdin.readline().rstrip()

# 상근 먼저
# 1 또는 3 => 홀수로 시작
# 다음은 짝수가 됨 => 1 또는 3 더하면 -> 2 또는 6이 됨
# 다음은 홀수가 됨 => 1또는 3 더하면 -> 3 또는 9가 됨
# 홀/ 짝/ 홀/ 짝
# 즉 홀이면 상근이가 가져가고
# 짝이면 창영이가 가져가는 듯
N = int(input())
if N%2 == 1 : print("SK")
else: print("CY")