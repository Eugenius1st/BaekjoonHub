#모든 점수를 점수/M*100
n= int(input())
arr = list(map(int,input().split()))
maxN = max(arr)
for i in range(len(arr)):
    arr[i] =  (arr[i] / maxN)*100
avg = sum(arr) / len(arr)
print(avg)