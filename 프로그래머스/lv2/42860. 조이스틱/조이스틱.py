def solution(name):
    
    # 조이스틱 조작 횟수
    answer = 0
    
    # 한 방향으로만 이동했을 때 좌우 이동 횟수
    moves = len(name) - 1
    
    for idx, alpha in enumerate(name):
    
        # 해당 알파벳 변경 최소값 추가
        answer += min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1)
    
        # 해당 알파벳 이후 연속된 A 문자열의 다음 인덱스 찾기 (문제에서 A가 기본 값이기 때문에 A를 찾음)
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
    
        """ min(기존 방식 / A 문자열 까지(idx) + 다시 왼쪽으로 진행(idx + len(name)-next) /
        A 문자열 까지(len(name)-next) + 다시 오른쪽으로 진행(len(name)-next + idx) """
        moves = min( [moves, idx + idx + ( len(name) - next ), idx + 2 * ( len(name) - next) ] )
    
    # 좌,우 이동의 최소값을 더해 줌.
    answer += moves
    return answer