A,B = map(int, input().split())

C = [0] * A
D = [0] * B

for i in range(A):
    str = input()
    for j in range(len(str)):
        if(str[j] == 'X'):
            C[i] = 1
            D[j] = 1

print(max(C.count(0),D.count(0)))