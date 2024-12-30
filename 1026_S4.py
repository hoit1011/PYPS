n = int(input())

arra = list(map(int,input().split()))
arrb = list(map(int,input().split()))

arra.sort()
arrb.sort(reverse=True)

cnt = 0

for i in range(n):
    cnt += arra[i] * arrb[i]

print(cnt)