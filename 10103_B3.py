x = int(input())

a = 100
b = 100
for i in range(x):
    A, B = map(int, input().split())
    if(A>B):
        b -= A
    elif(B > A):
        a -= B

print(a, b , sep='\n') # sep = 한줄씩 출력