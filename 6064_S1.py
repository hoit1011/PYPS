T = int(input())  

for _ in range(T):
    M, N, X, Y = map(int, input().split())
    
    answer = -1
    
    k = X
    while k <= M * N:
        if (k - 1) % N + 1 == Y:
            answer = k
            break
        k += M
    
    print(answer)
