import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input().strip()))

arr.sort()

cnt = N
answer = []
for i in range(N):
    answer.append(cnt * arr[i])
    cnt -= 1
print(max(answer))

sys.exit(0)