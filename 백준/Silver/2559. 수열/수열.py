import sys

N,K = map(int,input().split())
arr = list(map(int,input().split()))
accu = sum(arr[:K])
maxVal = accu

# 간격이 K 씩이니 합인 값에 i-K를 빼주자
for i in range(K,N):
    accu -= arr[i-K]
    accu += arr[i]
    #print(i-K,arr[i-K],i,arr[i])
    if(maxVal<accu):
        maxVal = accu


    #print(accu)
print(maxVal)



