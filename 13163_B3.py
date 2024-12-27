a = int(input())

for i in range(a):
    arr = list(input().split())
    arr[0] = "god"
    for j in range(len(arr)):
        print(arr[j],end="")
    print("")