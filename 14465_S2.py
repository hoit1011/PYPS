N,K,B = map(int,input().split())

arr = [0]*N
for i in range(B):
    a = int(input())
    arr[a-1] = 1

start = 0
end = K - 1
Sum = 0
for i in range(0, end+1):
    Sum += arr[i]

Max = 99999
while True:
    if(Max > Sum):
        Max = Sum
    if(end == N-1):
        break
    start += 1
    end += 1
    Sum -= arr[start-1]
    Sum += arr[end]

print(Max)
