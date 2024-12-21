a = int(input())

b = list(map(int, input().split()))

for i in range(a):
    if b[i] >= 300:
        print("1", end = " ")
    elif b[i] >= 275:
        print("2", end = " ")
    elif b[i] >= 250:
        print("3", end = " ")
    else:
        print("4", end = " ")

        