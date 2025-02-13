while True:
    try:
        s,t = map(str,input().split())
        cnt = 0
        for i in range(len(t)):
            if t[i] == s[cnt]:
                cnt += 1
            if len(s) == cnt:
                break

        if len(s) == cnt:
            print("Yes")
        else:
            print("No")
    except:
        break
