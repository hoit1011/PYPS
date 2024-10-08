n = str(input())
ok = False
for i in range(len(n) - 1):
    cnta = 1
    cntb = 1
    a = n[0:i+1]
    b = n[i+1:len(n)]
    for j in range(len(a)):
        cnta *= int(a[j])
    for j in range(len(b)):
        cntb *= int(b[j])
    if(cnta == cntb):
        ok = True
        break;

if ok == True:
    print("YES")
else:
    print("NO")

#깨달은점 : 곱하기였는데 cnta를 0으로 둔게 잘못됐었다 다음부턴 문제를 좀더 열심히 읽고 푸는 습관을 가져야겠다.