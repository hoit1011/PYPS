import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmon = {}
number = {}

for i in range(1, N+1):
    po = input().strip()
    poketmon[i] = po
    number[po] = i

for i in range(M):
    find = input().strip()
    if find[0].isalpha():
        print(number[find])
    else:
        print(poketmon[int(find)])