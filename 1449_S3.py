N, L = map(int,input().split())
li = list(map(int,input().split()))
li.sort()

start = li[0]
cnt = 1

for location in li[1:]:
    if location in range(start, start + L):
        continue
    else:
        start = location
        cnt += 1

print(cnt)