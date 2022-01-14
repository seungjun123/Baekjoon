import sys
N = int(sys.stdin.readline())
List = []

for i in range(N):
    List.append(list(map(int, sys.stdin.readline().split())))

for i in sorted(List):
    print(i[0],i[1])