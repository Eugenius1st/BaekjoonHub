answer = []
def dfs(visited, tickets, start_ticket, trip):
    global answer
    if len(trip) == len(tickets):
        new_answer = []
        for i in range(len(trip)):
            new_answer.append(trip[i][0])
        new_answer.append(trip[-1][1])
        
        if len(answer) == 0:
            answer = new_answer
        else:     
            for i in range(len(answer)): 
                if new_answer[i] == answer[i] : continue
                elif new_answer[i] < answer[i]: answer = new_answer
                else: break

    for i in range(len(tickets)):
        if tickets[i][0] == start_ticket[1] and not(visited[i]):
            visited[i] = True
            trip.append(tickets[i])
            dfs(visited, tickets, tickets[i], trip)
            visited[i] = False
            trip.pop()
def solution(tickets):
    # 중복으로 담기는 경우도 있으니 visited 에 비행기표를 담는게 아니라 T/F 로 넣어 두자!
    start_ticket = []
    visited = [False] * len(tickets)
    tickets.sort()

    for i in range(len(tickets)):
        trip = []
        if tickets[i][0] == "ICN":
            start_ticket = tickets[i]
            visited[i] = True
            trip.append(start_ticket)
            dfs(visited, tickets, start_ticket, trip)
            visited[i] = False
            trip.pop()
    print("answer",answer)

    return answer
