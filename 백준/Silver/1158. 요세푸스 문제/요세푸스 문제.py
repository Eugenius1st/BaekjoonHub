import sys

# BOJ__1158__원형큐
N,K = map(int,input().split())
arr = list(range(N+1))
res = []
size = N+1
front = 0
rear = size-1
tmp = 0
cnt = 0
def enqueue(x):
    global rear
    if (rear+1)%size != front:#is not full
        rear = (rear+1)%size
        arr[rear] = x

def dequeue():
    global front
    if front == rear: #is empty
        print("<"+", ".join(map(str,res))+", "+tmp+">")
        sys.exit()
    else:
        front = (front+1)%size
        save = arr[front]
        arr[front]=None
        return save

while front!=rear:
    cnt += 1
    tmp = dequeue()
    if cnt == K:
        cnt = 0
        res.append(tmp)
    else:
        enqueue(tmp)

print("<"+", ".join(map(str,res))+">")