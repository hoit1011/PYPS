# N = list(map(int, input().split()))
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# A.extend(B)
# A.sort()

# answer = ' '.join(map(str, A))
# print(answer)

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
arr = []
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(len(A)):
    arr.append(A[i])

for i in range(len(B)):
    arr.append(B[i])

arr.sort()

for i in range(len(arr)):
    print(arr[i],end=" ")