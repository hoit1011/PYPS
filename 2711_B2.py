x = int(input())

for _ in range(x):
    N, S = input().split()
    N = int(N)
    print(S[:N-1], S[N:] , sep='') # S[:N-1] = N-1번쨰 문자 전까지 / S[N:] = N번째 문자 뒤부터