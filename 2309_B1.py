arr = []

for i in range(9):
    a = int(input())
    arr.append(a)


for i in range(9):
    for j in range(9):
        cnt = 0
        arr2 = []
        for k in range(9):
            if(i == j):
                continue
            if(k == i):
                continue
            if(k == j):
                continue
            cnt += arr[k]
            arr2.append(arr[k])
        if(cnt == 100):
            arr2.sort()
            for i in range(len(arr2)):
                print(arr2[i])
            exit()