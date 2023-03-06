answer = 0
def DFS(node, sumNum, final, numbers, target):
    global answer
    if node == final:
        if sumNum == target:
             answer += 1
    else:
        tmpNum = numbers[node]
        DFS(node+1, sumNum+tmpNum, final, numbers, target)
        DFS(node+1, sumNum-tmpNum, final, numbers, target)        
    
def solution(numbers, target):
    final = len(numbers)
    
    # node, sunNum, final, numbers, target
    DFS(0, 0, final, numbers, target) 
    return answer
