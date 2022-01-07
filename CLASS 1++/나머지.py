answer = []

for i in range(0, 10):
    A = int(input())
    answer.append(A%42)

print(len(set(answer)))