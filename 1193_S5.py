N = int(input())

L, R = 1,0
LR = False
for i in range(N):
    if(i == 0):
        R += 1
        continue
    elif(LR == False and L == 1):
        LR = True
        R += 1
    elif(LR == True and R == 1):
        LR = False
        L += 1
    elif(LR == False and L != 1):
        L -= 1
        R += 1
    elif(LR == True and R != 1):
        R -= 1
        L += 1

    

print(f'{L}/{R}')