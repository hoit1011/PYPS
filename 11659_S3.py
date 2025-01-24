import sys
input = sys.stdin.readline

n, m = map(int,input().split())
numbers = list(map(int,input().split()))
Sum = [0]
tmp = 0

for i in numbers:
    tmp += i
    Sum.append(tmp)

for i in range(m):
    a,b = map(int,input().split())
    print(Sum[b] - Sum[a-1])