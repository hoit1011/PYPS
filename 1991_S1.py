N = int(input())

tree = [[-1,-1] for _ in range(N)]
for i in range(N):
    li = list(input().split())
    S = ord(li[0]) - 65
    if li[1] != '.':
        tree[S][0] = ord(li[1]) - 65
    if li[2] != '.':
        tree[S][1] = ord(li[2]) - 65

def front(node):
    if node == -1:
        return
    print(chr(node+65),end='')
    front(tree[node][0])
    front(tree[node][1])

def mid(node):
    if node == -1:
        return
    mid(tree[node][0])
    print(chr(node+65),end='')
    mid(tree[node][1])

def back(node):
    if node == -1:
        return
    back(tree[node][0])
    back(tree[node][1])
    print(chr(node+65),end='')

front(0)
print()
mid(0)
print()
back(0)