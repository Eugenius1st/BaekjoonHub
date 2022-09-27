def solution(n,times):
    start,end = 1,max(times)*n
    res = end
    while start <= end:
        people = 0
        mid = (start+end)//2
        for time in times:
            people += mid//time
        if people < n:
            start = mid+1
        else:
            end = mid-1
            res = min(res,mid)
    return res