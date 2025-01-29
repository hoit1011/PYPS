N = int(input())
arr = [0] * N

if(N == 1):
    print("1")
    exit()
    
arr[0] = 1
arr[1] = 2
for i in range(2,N):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[N-1] % 10007)