N = int(input())
S = input()
sum = 0

for i in range(N):
    sum += (ord(S[i])-96) * (31**i)

print(sum%1234567891)