S = input()
li = list(map(str, S.split(".")))
cnt = len(li) - 1
arr = []
for i in range(len(li)):
    if len(li[i]) % 2:
        print("-1")
        exit()
    else:
        arr.append(len(li[i]))

for i in range(len(arr)):
    a = arr[i] // 4
    b = arr[i] // 2 - (a * 2)
    for j in range(a):
        print("AAAA",end="")
    for j in range(b):
        print("BB",end="")
    
    if(i < len(arr) -1):
        print(".",end="")
