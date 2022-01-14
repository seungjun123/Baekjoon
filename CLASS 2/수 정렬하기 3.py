import sys
N = int(sys.stdin.readline())
num = [0] * 10001

for i in range(N):
    num[int(sys.stdin.readline())] += 1

for i in range(len(num)):
    while num[i] > 0:
        print(i)
        num[i] -= 1