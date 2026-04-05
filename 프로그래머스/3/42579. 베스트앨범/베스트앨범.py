def solution(genres, plays):
    answer = []
    
    # 배열 튜플로 저장할 수 있나? classic: [(500,1)] => 가능
    # 해시 두개 만들어서 첫번째는 합 기준 해시
    # 두번째는 튜플 담은 해시
    
    sumInfo = {} # 장르 : 합
    for i in range(len(genres)):
        sumInfo[genres[i]] = sumInfo.get(genres[i], 0) + plays[i]
    
    tmpG = []
    for j in sumInfo:
        tmpG.append((j,sumInfo[j]))
    arrG = sorted(tmpG, key=lambda x: x[1], reverse=True)
    
    # print("arrG",arrG) # 장르 전체합으로 정렬된 배열
    
    # 장르별 노래 정리
    songPerGenre = {}
    for z in range(len(genres)):
        if genres[z] not in songPerGenre:
            songPerGenre[genres[z]] = []    
        songPerGenre[genres[z]].append((z, plays[z]))
    
    print("songPerGenre",songPerGenre)
    
    sortedPerGenre = {} # 키별 노래 재생 수 높은순 딕셔너리 정렬
    for x in songPerGenre:
        sortedPerGenre[x] = sorted(songPerGenre[x], key=lambda x : x[1], reverse = True) 
        
    for y in arrG: #classic, pop...
        genre = y[0]
        cnt = 0
        for song in sortedPerGenre[genre]:
            if cnt > 1 : break
            answer.append(song[0])
            cnt += 1
    return answer