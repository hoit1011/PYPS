# n = int(input())

# arr = list(map(int, input().split()))

# cnt = 0
# max = 0
# min = 0

# for i in range(len(arr)-1):
#     if(i == 0):
#         cnt = arr[i]
#         min = arr[i]

#     if(arr[i] <= cnt):
#         if(max < arr[i-1] - min):
#             max = arr[i-1] - min
#         min = arr[i]
#         cnt = arr[i]
#     elif(cnt < arr[i]):
#         cnt = arr[i]

# if(arr[n-1] - min > max):
#     print(arr[n-1] - min)
# else:
#     print(max)

n = int(input())
arr = list(map(int, input().split()))

a = 0
b = []

for i in(range(n-1)):
    if(arr[i] < arr[i+1]):
        a += arr[i+1] - arr[i]
    else:
        b.append(a)
        a = 0

b.append(a)
print(max(b))