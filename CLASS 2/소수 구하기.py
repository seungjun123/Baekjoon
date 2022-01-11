M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue

    sosu = True

    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            sosu = False
            break

    if sosu == True:
        print(i)