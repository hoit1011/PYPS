N = int(input())

s = input()

color = s[0]
last = 0
for i in range(N):
    if(s[i] == color):
        last = i
cnt = 1
if last + 1 != N:
    cnt += 1
for i in range(1,last):
    if s[i-1] == color and s[i] != color:
        cnt += 1

print(cnt)