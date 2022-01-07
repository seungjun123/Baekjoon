mul = 1
for i in range(0, 3):
    mul *= int(input())

mul = str(mul)

for i in range(0, 10):
    print(mul.count(str(i)))