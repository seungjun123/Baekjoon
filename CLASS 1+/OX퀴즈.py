N = int(input())

for i in range(N):
    count = 1
    sum = 0
    test = input()

    for j in range(len(test)):
        if(test[j] == 'O'):
            sum += count
            count += 1
        else:
            count = 1
    
    print(sum)