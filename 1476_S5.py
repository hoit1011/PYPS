E,S,M = map(int,input().split())

cnt = 1
a,b,c = 1,1,1
while True:
    if(a == E and b == S and c == M):
        break
    a += 1
    b += 1
    c += 1
    if(a == 16):
        a = 1
    if(b == 29):
        b = 1
    if(c == 20):
        c = 1
    cnt += 1


print(cnt)