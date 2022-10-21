import sys

N = int(input())
roads = list(map(int,input().split()))
gs_caltex = list(map(int,input().split()))


def answer(N,roads,gs_caltex):
    # 첫번째 값 더하기
    min_price = roads[0] * gs_caltex[0]
    # 가장 값이 싼 주유소 지정
    min_cost = gs_caltex[0]
    for i in range(1, N-1):
        if min_cost > gs_caltex[i]: # 가장 값이 싼 주유소가 현재 주유소 보다 비싸면 바꿔준다.
            min_cost = gs_caltex[i] # 값 싼 주유소로 바꿔주기
        min_price += min_cost * roads[i]

    print(min_price)


answer(N,roads,gs_caltex)
