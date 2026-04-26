import heapq

def solution(scoville,k):
    scov = scoville[:]
    heapq.heapify(scov) # heapify 는 리턴값 없음 그냥 힙화
    
    answer = 0
    while scov[0] < k:
        answer += 1
        newScov = heapq.heappop(scov) + (heapq.heappop(scov)*2)
        heapq.heappush(scov, newScov)
        if len(scov)==1 and scov[0] < k: 
            return -1
        
    return answer