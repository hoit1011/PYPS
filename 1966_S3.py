n = int(input())

for _ in range(n):
    n,m = map(int,input().split())
    li = list(map(int,input().split()))

    result = 1
    while li:
        if li[0] < max(li):
            li.append(li.pop(0))
        else:
            if(m == 0):
                break
            li.pop(0)
            result += 1
        
        m = m - 1 if m > 0 else len(li) - 1

    print(result)