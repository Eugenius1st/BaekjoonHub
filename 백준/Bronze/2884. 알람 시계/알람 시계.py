H,M = map(int,input().split())
#45
if M < 45 :
    M = (M+60) - 45
    H = H-1
    if H < 0:
        H = 24 + H
else: 
    M = M - 45
print(H,M)