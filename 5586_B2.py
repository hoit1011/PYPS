s = list(input()) # 배열도 list()로 받아야한다
a,b = 0 , 0
for i in range(len(s)-2): # .length나 .size가 아닌 len() 이다 
    if s[i] == 'J' and s[i+1] == 'O' and s[i+2] == 'I' :
        a += 1
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I' :
        b += 1

print(a,b,sep='\n')