N = int(input())
s_list = []

for i in range(N):
    x, y = map(int, input().split())
    s_list.append((x, y))

for i in s_list:
    cnt = 1
    for j in s_list:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')