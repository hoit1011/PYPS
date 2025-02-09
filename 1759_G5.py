import sys
input = sys.stdin.readline
from itertools import combinations

L,C = map(int,input().split())
li = list(map(str,input().split()))
li.sort()
arr = {'a':0,'e':0,'i':0,'o':0,'u':0}

for combination in combinations(li,L):
    j = 0
    m = 0
    for i in combination:
        if i in arr:
            m += 1
        else:
            j += 1
    if m >= 1 and j >= 2:
        print(''.join(map(str,combination)))

sys.exit(0)