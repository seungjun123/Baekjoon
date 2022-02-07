from sys import stdin
N = stdin.readline()
N_list = set(stdin.readline().split())
M = stdin.readline()
M_list = stdin.readline().split()

for i in M_list:
    print(1) if i in N_list else print(0)