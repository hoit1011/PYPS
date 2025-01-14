import sys
input = sys.stdin.readline

a,b = map(int,input().split())
d = {}
for _ in range(a):
    Str = input().strip()
    d[Str] = 0

cnt = 0

for i in range(b):
    Str = input().strip()
    if(Str in d):
        cnt += 1

print(cnt)