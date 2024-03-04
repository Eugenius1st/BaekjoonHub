text = str(input())
cAlpha = {"c=":"č","c-":"ć","dz=":"dž","d-":"đ","lj":"lj","nj":"nj","s=":"š","z=":"ž"}
res = 0
temp = ""
for i in text:
    temp = temp + i
    if temp == "dz=":
        res += 1
        temp = ""
    if temp == "dz":
        continue
    if len(temp) == 2:
        if temp in cAlpha:
            res += 1
            temp =""
        else:
            res += 1
            temp = temp[1:]
    if len(temp) == 3 and temp != "dz=":
        res += 1
        temp = temp[1:]
        if temp in cAlpha:
            res += 1
            temp =""
        else:
            res += 1
            temp = temp[1:]
print(res+len(temp))
