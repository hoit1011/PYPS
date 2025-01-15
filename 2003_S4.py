import sys
input = sys.stdin.readline

a, b = map(int,input().split())
li = list(map(int,input().split()))


start = 0
end = 0
Sum = li[0]

cnt = 0

while True:
    if Sum == b:
        cnt += 1
    
    if Sum >= b:
        start += 1
        Sum -= li[start - 1]
    else:
        if end == a-1:
            break
        end += 1
        Sum += li[end]

print(cnt)