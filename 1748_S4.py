N = int(input())
cnt = 0
a = 9
b = 1
while N > a:
    cnt += (a * b)
    N -= (a)
    a *= 10
    b += 1

cnt += (N * b)
print(cnt)