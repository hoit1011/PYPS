import sys
input = sys.stdin.readline

N = int(input())
btn = int(input())
li = list(map(int, input().split()))

min_ans = abs(N-100)

for i in range(1000001):
    nums = str(i)
    for j in range(len(nums)):
        if int(nums[j]) in li:
            break
        elif j == len(nums) - 1:
            min_ans = min(min_ans,abs(i - N) + len(nums))

print(min_ans)