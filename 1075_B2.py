N = int(input())
F = int(input())

a = int(str(N)[len(str(N))-2:])

for i in range(N - a,N + 100):
    if i % F == 0:
        print(str(i)[len(str(N))-2:])
        break