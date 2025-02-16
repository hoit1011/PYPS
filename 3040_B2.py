from itertools import combinations
arr = []
for _ in range(9):
    arr.append(int(input()))

for combination in combinations(arr,2):
    if sum(arr) - sum(combination) == 100:
        for i in range(9):
            if arr[i] not in combination:
                print(arr[i])