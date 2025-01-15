from itertools import permutations

N = int(input())

li = list(map(int,input().split()))

Max = 0
for i in permutations(li):
    li2 = list(i)
    numli = []
    for j in range(N):
        numli.append(li2[j])
    cnt = 0
    for j in range(0,N - 1):
        cnt += abs(numli[j] - numli[j+1])
    if(cnt > Max):
        Max = cnt

print(Max)

