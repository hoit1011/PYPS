N = int(input())

arr = [0,1]

for i in range(2,N+1):
    arr.append(arr[i-1]+arr[i-2])

print(arr[N])