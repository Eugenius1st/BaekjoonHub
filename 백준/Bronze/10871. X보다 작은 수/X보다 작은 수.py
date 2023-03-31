a,b = map(int,input().split())
text = list(map(int,input().split()))

for i in text:
    if i < b:
        print(i, end= " ")