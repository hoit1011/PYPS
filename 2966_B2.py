n = int(input())
arr = list(input())

Adrian = ['A','B','C']
Bruno = ['B','A','B','C']
Goran = ['C','C','A','A','B','B']

Adrian_num = 0
Bruno_num = 0
Goran_num = 0

for i in range(n):
    if(arr[i] == Adrian[i % len(Adrian)]):
        Adrian_num += 1
    if(arr[i] == Bruno[i % len(Bruno)]):
        Bruno_num += 1
    if(arr[i] == Goran[i % len(Goran)]):
        Goran_num += 1

print(max(Adrian_num,Bruno_num,Goran_num))

if(max(Adrian_num,Bruno_num,Goran_num) == Adrian_num):
    print('Adrian')
if(max(Adrian_num,Bruno_num,Goran_num) == Bruno_num):
    print('Bruno')
if(max(Adrian_num,Bruno_num,Goran_num) == Goran_num):
    print('Goran')
