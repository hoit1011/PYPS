n = list(map(int, input().split()))

n.sort()

n1 = n[1] - n[0]
n2 = n[2] - n[1]

if(n1 == n2):
    print(n[2] + n1)
elif(n1 > n2):
    print(n[0] + n2)
else:
    print(n[1] + n1)