import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
li.sort()

result = 1

for i in range(N):
    if result < li[i]:
        break
    result += li[i]

print(result)
