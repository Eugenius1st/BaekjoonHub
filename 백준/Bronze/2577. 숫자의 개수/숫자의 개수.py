dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
n = 1
while True:
    try:
        n *= int(input())
    except EOFError:
        break

while n > 0:
    tmp = n % 10
    dict[tmp] += 1
    n //= 10

for i in range(10):
    print(dict[i])