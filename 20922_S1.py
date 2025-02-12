N, K =map(int,input().split())
li = list(map(int,input().split()))

left = 0
right = 0
d = {}

Max = 0
while right != N:
    if(li[right] not in d):
        d[li[right]] = 0
    
    if d[li[right]] > K -1:
        d[li[left]] -= 1
        left += 1
    else:
        d[li[right]] += 1
        right += 1
        Max = max(right - left,Max)

print(Max)
