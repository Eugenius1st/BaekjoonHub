import sys
arr = list(range(int(input())+1))
arrSize = len(arr)
front = 0
rear = arrSize-1
tmp = 0

def enqueue(x):
    global rear
    if (rear+1)%arrSize != front:#is not full
        rear = (rear+1)%arrSize
        arr[rear]=x

def dequeue():
    global front
    if front == rear:#empty
        print(tmp)
        sys.exit()
    front = (front+1)%arrSize
    save = arr[front]
    arr[front] = ""
    return save



while rear!=front:
    tmp = dequeue()
    tmp = dequeue()
    if(rear==front):
        break
    enqueue(tmp)
print(tmp)
