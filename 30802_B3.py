n = int(input())
A = list(map(int, input().split()))
B , C= map(int,input().split())

count = 0
for i in range(6):
    if(A[i] % B == 0):
        count += int(A[i] / B)
    else:
        count += int(A[i] / B ) + 1

print(count)
print(f'{int(n / C)} {n % C}')