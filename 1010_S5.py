def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    bridge = factorial(b) // (factorial(a) * factorial(b - a))
    print(bridge)