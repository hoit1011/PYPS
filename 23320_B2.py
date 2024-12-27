n = int(input())

arr = list(map(int, input().split()))

a, b = map(int, input().split())
cnt = 0
for i in range(len(arr)):
    if (arr[i] >= b):
        cnt += 1

print(int(n/(100/a)), end=" ")
print(cnt)
