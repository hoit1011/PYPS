N = int(input())

d = {}
for i in range(N):
    S = input()
    if S not in d:
        d[S] = 0
    d[S] += 1

MaxValue = max(d.values())

arr = []
for i in d.items():
    a,b = i
    if b == MaxValue:
        arr.append(a)

arr.sort()

print(arr[0])
