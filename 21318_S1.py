import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
arr = [0] * N
for i in range(len(li)-1):
    if li[i] > li[i+1]:
        arr[i] = 1

prefix_sum = [0] * (N+1)
for i in range(1,N+1):
    prefix_sum[i] = arr[i-1] + prefix_sum[i-1]

Q = int(input())
for i in range(Q):
    A,B = map(int,input().split())
    print(prefix_sum[B-1] - prefix_sum[A-1])
