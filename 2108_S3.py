N = int(input())
num = []
All = 0
d = {}
for i in range(N):
    n = int(input())
    num.append(n)
    All += n
    if n in d:
        d[n] += 1    
    else:
        d[n] = 1

num.sort()

mx = max(d.values())
maxarr = []
for i in d:
    if mx == d[i]:
        maxarr.append(i)

maxarr.sort()

print(round(All / N))

print(num[round(N/2)])

if(len(maxarr) == 1):
    print(maxarr[0])
else:
    print(maxarr[1])

print(num[-1] - num[0])