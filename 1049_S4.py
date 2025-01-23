N,M = map(int,input().split())

six = []
one = []

for _ in range(M):
    a,b = map(int,input().split())
    six.append(a)
    one.append(b)

sixmin = min(six)
onemin = min(one)

namuji = N % 6
mok = N // 6
cost1 = N * onemin

cost2 = ((N // 6) + 1) * sixmin

cost3 = (N // 6) * sixmin + (N % 6) * onemin

print(min(cost1,cost2,cost3))
