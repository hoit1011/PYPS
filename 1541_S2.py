S = input().split('-')

num = []

for i in S:
    Sum = 0
    tmp = i.split("+")
    for j in tmp:
        Sum += int(j)
    num.append(Sum)

cnt = num[0]

for i in range(1,len(num)):
    cnt -= num[i]
print(cnt)