while(1):
    N = list(map(int, input().split()))
    if(max(N) == 0):
        break

    M = max(N)
    N.remove(max(N))
    
    if(N[0]**2 + N[1]**2 == M**2):
        print("right")
    else:
        print("wrong")