n = int(input())

for i in range(n):
    x = list(map(str, input().split()))
    num = float(x[0])
    
    for i in range(len(x)):
        if i == 0:
            continue
        if(x[i] == '@'):
            num *= 3
        elif(x[i] == '%'):
            num += 5
        elif(x[i] == '#'):
            num -= 7
    print("%.2f" % num)