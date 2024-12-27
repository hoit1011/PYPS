str = input()

cnt = 0
for i in range(len(str)):
    if str[i] in('A','B','C'):
        cnt += 3
    elif str[i] in('D','E','F'):
        cnt += 4
    elif str[i] in('G','H','I'):
        cnt += 5
    elif str[i] in('J','K','L'):
        cnt += 6
    elif str[i] in ('M','N','O'):
        cnt += 7
    elif str[i] in ('P','Q','R','S'):
        cnt += 8
    elif str[i] in ('T','U','V'):
        cnt += 9
    elif str[i] in ('W','X','Y','Z'):
        cnt += 10

print(cnt)

