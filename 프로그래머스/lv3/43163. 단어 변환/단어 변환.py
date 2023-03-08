minLen = 2147000000
def DFS(begin, target, words,visited):
    global minLen
    visited.append(begin)
    #print(visited)
    if begin == target:
        minLen = min(minLen,len(visited)-1)
    else:
        for i in range(len(words)):
            cnt = 0

            if words[i] not in visited:
                for j in range(len(begin)):
                    if begin[j] != words[i][j]:
                        cnt += 1
                        if cnt > 1 : 
                            cnt = 0
                            break
                if cnt == 1:
                    DFS(words[i],target,words,visited)
                    visited.pop()                    
                    cnt = 0


def solution(begin, target, words):
    visited = []
    if target not in words: return 0
    if begin == target: return 1
    DFS(begin, target, words,visited)
    answer = 0
    if minLen != 2147000000: answer = minLen
    print(answer)
    return answer