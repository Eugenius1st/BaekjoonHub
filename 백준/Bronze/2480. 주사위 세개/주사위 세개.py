A,B,C = map(int,input().split())
res = 0
if A==B==C:
    res = 10000+(A)*1000
elif A==B or C==A :
    res = 1000+(A)*100
elif B==C:
    res = 1000+(B)*100
else:
    res = max(A,B,C)*100

print(res)