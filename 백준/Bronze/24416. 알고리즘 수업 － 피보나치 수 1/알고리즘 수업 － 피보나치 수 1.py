import sys
#from collections import deque
#sys.stdin=open("input.txt", "rt")
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1+=1
        return 1  # 코드1
    else: return fib(n - 1) + fib(n - 2);

def fibonacci(n):
    global cnt2
    fibo = [0]*n
    fibo[1]=1
    fibo[2]=1
    for i in range(3,n):
        cnt2+=1
        fibo[i] = fibo[i - 1] + fibo[i - 2]  # 코드2

if __name__ == "__main__":
    n = int(input())
    cnt1=0
    cnt2 =1
    fib(n)
    fibonacci(n)
    print (cnt1,cnt2)
   