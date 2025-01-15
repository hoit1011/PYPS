N = int(input())

arr = []
for i in range(N):
    Str = int(input())
    arr.append(Str)
count = 0
arr.reverse()
for i in range(N):
    if i == 0:
        continue
    if(arr[i] >= arr[i-1]):
        cnt = arr[i-1]-1
        count += arr[i] - cnt
        arr[i] = cnt
print(count)