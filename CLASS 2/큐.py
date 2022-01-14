import sys

N = int(sys.stdin.readline())
queue = []

for i in range(N):
    S = sys.stdin.readline().split()
    
    if S[0] == 'push':
        queue.append(S[1])
    elif S[0] == 'pop':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue.pop(0))
    elif S[0] == 'size':
        print(len(queue))
    elif S[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif S[0] == 'front':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[0])
    elif S[0] == 'back':
        if len(queue) < 1:
            print(-1)
        else:
            print(queue[len(queue)-1])