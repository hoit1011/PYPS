import sys
input = sys.stdin.readline

N = int(input())
li = list(map(str, input().split()))
d = {}
for i in range(N):
    d[li[i]] = 0

n = int(input())
li2 = list(map(str, input().split()))

for i in range(n):
    if(li2[i] in d):
        print("1",end=" ")
    else:
        print("0",end=" ")
