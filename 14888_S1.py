import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int,input().split()))
op = list(map(int, input().split()))

max_res = - int(1e9)
min_res = int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global max_res, min_res
    if depth == N:
        max_res = max(max_res,total)
        min_res = min(min_res,total)
        return
    if plus:
        dfs(depth + 1,total+li[depth],plus-1,minus,multiply,divide)
    if minus:
        dfs(depth + 1,total-li[depth],plus,minus-1,multiply,divide)
    if multiply:
        dfs(depth + 1,total*li[depth],plus,minus,multiply-1,divide)
    if divide:
        dfs(depth + 1, int(total / li[depth]), plus, minus, multiply, divide - 1)

dfs(1,li[0],op[0],op[1],op[2],op[3])

print(max_res)
print(min_res)