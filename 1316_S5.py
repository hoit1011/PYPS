N = int(input())

cnt = 0
for _ in range(N):
    check = True
    Str = input()
    d = {}
    for i in range(len(Str)):
        if i == 0:
            d[Str[i]] = 0

        elif Str[i] in d:
            if Str[i-1] == Str[i]:
                continue
            else:
                check = False
        else:
            d[Str[i]] = 0
    
    if check:
        cnt += 1
print(cnt)
    