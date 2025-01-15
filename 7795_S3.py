N = int(input())
for _ in range(N):
    a, b = map(int,input().split())
    num = list(map(int,input().split()))
    num2 = list(map(int,input().split()))
    num.sort(reverse=True)
    num2.sort(reverse=True)
    count = 0
    start = 0
    for i in range(a):
        for j in range(start,b):
            if(num[i] > num2[j]):
                count += b-j
                break
            else:
                start += 1
    print(count)