A, B = map(int, input().split())
C = A
D = B

while B > 0:
    A, B = B, A % B
    
print(A)
print(C * D // A)