
if __name__ == '__main__':
    N = int(input())
    arr= [0]
    result = []
    for i in range(N):
        arr.append(int(input()))
    arr.append(0)
    for i in range(1, N+1):
        if arr[i-1] <= arr[i] and arr[i] >= arr[i+1]:
            result.append(i)
    print(*result, sep="\n")