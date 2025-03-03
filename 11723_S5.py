import sys
input = sys.stdin.readline

N = int(input())
s = set()

for _ in range(N):
    li = input().split()
    a = li[0]

    if a == 'add':
        s.add(int(li[1]))
    if a == 'remove':
        s.discard(int(li[1]))
    if a == 'check':
        print(1 if int(li[1]) in s else 0)
    if a == 'toggle':
        x = int(li[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    if a == 'all':
        s = set(range(1,21))
    if a == 'empty':
        s.clear()