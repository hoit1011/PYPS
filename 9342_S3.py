N = int(input())

for i in range(N):
    S = input()
    check = True
    if S[0] not in {'A','B','C','D','E','F'}:
        check = False
    
    for j in range(1,len(S)):
        if S[j] == 'A':
            if S[j-1] == 'A':
                continue
            elif j-1 == 0:
                continue
            else:
                check = False
        elif S[j] == 'F':
            if S[j-1] == 'A' or S[j-1] == 'F':
                continue
            else:
                check = False
        elif S[j] == 'C':
            if S[j-1] == 'F' or S[j-1] == 'C':
                continue
            else:
                check = False
        elif j == len(S) -1:
            if S[j] in {'A','B','C','D','E','F'}:
                continue
            else:
                check = False
        else:
            check = False
            break
    if check:
        print("Infected!")
    else:
        print("Good")
