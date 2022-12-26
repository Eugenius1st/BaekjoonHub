import sys
#sys.stdin = open("input.txt", "rt")
def input():
    return sys.stdin.readline().rstrip()

def findFunc(val):
    for i in range(2,N+1):
        stack[i]=stack[i-1]+1
        if i % 2 ==0 and stack[i]> stack[i//2]+1:
            stack[i]=stack[i//2]+1
        if i % 3 ==0 and stack[i]> stack[i//3]+1:
            stack[i]=stack[i//3]+1
    print(stack[val])

if __name__ == "__main__":
    N = int(input())
    stack = [0]*(N+1)
    findFunc(N)
