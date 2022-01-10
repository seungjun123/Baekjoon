from sys import stdin

N = int(stdin.readline())
words = []

for i in range(0, N):
    words.append(stdin.readline())

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(''.i)