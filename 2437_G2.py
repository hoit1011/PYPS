N = int(input())
li = list(map(int,input().split()))
li.sort()
print(li)
result = 1

for i in range(N):
    if result < li[i]:
        break
    result += li[i]

print(result)
