T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if(N % H == 0):
        YY = H
        XX = int(N / H)
    else:
        YY = N % H
        XX = int(N / H) + 1
    print('{1}{2:0>2}'.format('right', YY, XX))