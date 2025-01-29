N = int(input())
arr = []

Max = 0
for i in range(N):
    n = int(input())
    arr.append(n)
    Max = max(arr)

li = [0] * Max
li[0] = 1
li[1] = 2
li[2] = 4

for i in range(3,Max):
    li[i] = li[i-1] + li[i-2] +li[i-3]

for i in range(N):
    print(li[arr[i]-1])