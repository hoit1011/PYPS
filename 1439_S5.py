S = input()

cnt = 1

for i in range(len(S)):
    if i == 0:
        continue
    if S[i] != S[i-1]:
        cnt += 1

print(cnt // 2)