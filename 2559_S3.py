a,b = map(int,input().split())
arr = list(map(int,input().split()))

Max = -999999999999
start = 0
end = b - 1
Sum = 0
for i in range(start,end + 1):
    Sum += arr[i]
while True:
    if(Max < Sum):
        Max = Sum
    if(end == a-1):
        break
    start += 1
    end += 1
    Sum -= arr[start-1]
    Sum += arr[end]

print(Max)
