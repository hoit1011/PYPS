for i in range(3):
    n = int(input())
    a = 0
    cnt = 0
    for j in range(n):
        a = int(input())
        cnt += a;
    if cnt == 0:
        print("0")
    elif cnt < 0:
        print("-")
    elif cnt > 0:
        print("+")