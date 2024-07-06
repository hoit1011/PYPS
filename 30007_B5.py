x = int(input())
for i in range(x) :
    A,B,X= map(int, input().split())
    print(A * (X - 1) + B)