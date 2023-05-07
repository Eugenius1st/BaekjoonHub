x, y, w, h = map(int,input().split())


res = min(x,y,abs(w-x),abs(h-y))
print(res)