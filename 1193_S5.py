N = int(input())

line = 1
count = 1

while N > count:
    line += 1
    count += line

position = N - (count - line)
if line % 2 == 0:
    a = position
    b = line - position + 1
else:
    a = line - position + 1
    b = position

print(f"{a}/{b}")