A = int(input())

for i in range(0, A):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    index = [0] * N
    index[M] = 1
    count = 0
    
    while(1):
        if queue[0] == max(queue):
            count += 1

            if index[0] != 1:
                del queue[0]
                del index[0]
            else:
                print(count)
                break
        else:
            queue.append(queue.pop(0))
            index.append(index.pop(0))