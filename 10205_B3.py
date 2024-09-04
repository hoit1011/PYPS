# 한줄평 : int형이랑 string형을 한번에 출력하면 에러가 난다는걸 배웠고 .count로 원하는값만 뽑아올수 있다는걸 암 개쩜 ㄹㅇ

a = int(input())

for i in range(a):
    x = int(input())
    arr = input()
    b = arr.count('b')
    c = arr.count('c')
    print("Data Set " + str(i + 1) + ":")
    print(x - b + c)
    print()