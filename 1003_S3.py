# N = int(input())

# for i in range(N):
#     a = int(input())
#     zero = 0
#     one = 0

#     def fibonacci(n):
#         global zero, one 
#         if n == 0:
#             zero += 1
#             return 0
#         elif n == 1:
#             one += 1
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)

#     fibonacci(a)

#     print(zero, one)

N = int(input())

for i in range(N):
    a = int(input())
    
    zero_calls = [1,0]
    one_calls = [0,1]

    for i in range(2,a+1):
        zero_calls.append(zero_calls[i-1]+zero_calls[i-2])
        one_calls.append(one_calls[i-1]+one_calls[i-2])

    print(zero_calls[a],one_calls[a])