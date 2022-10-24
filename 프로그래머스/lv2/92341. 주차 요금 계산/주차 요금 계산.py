import sys


def input():
    return sys.stdin.readline().rstrip()

def solution(fees, records):
    carRecord = dict()
    maxTime = 1439
    res = dict()
    answer = []
    for x in records:
        info = x.split(" ")

        if info[2]=="IN":
            inTime=info[0].split(":")
            carRecord[info[1]] = int(inTime[0])*60 + int(inTime[1])
        else:
            outTmp=info[0].split(":")
            outTime = int(outTmp[0])*60 + int(outTmp[1])
            parkingTime = outTime - carRecord[info[1]]
            if info[1] in res: res[info[1]] += parkingTime
            else: res[info[1]] = parkingTime
            del carRecord[info[1]]
    if carRecord: #비어있지 않다면
        for key in carRecord:
            if key in res: res[key] += maxTime-carRecord[key]
            else: res[key] = maxTime-carRecord[key]
    
    
    for key in res:
        parkingTime = res[key]
        parkingFee = 0
        if parkingTime > fees[0]:
            parkingTime -= fees[0]
            parkingFee += fees[1]
            if parkingTime > 0:
                fee = parkingTime // fees[2]
                parkingTime %= fees[2]
                parkingFee += fee * fees[3]
                if parkingTime > 0:
                    parkingFee += fees[3]
        else: parkingFee = fees[1]
        res[key] = parkingFee 
        #차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return    
    
    tmp = sorted(res.items(), key = lambda item: int(item[0]))
    answer = [x[1] for x in tmp]
    print(answer)
    return answer

    # 차량 번호가 작은 자동차부터 요금 배열에 담아서 return
