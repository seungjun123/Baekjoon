N = int(input())
layer = 1
a = 1

while 1:
    if N / layer > 1:
        layer += 6*a
        a += 1
    else:
        print(a)
        break