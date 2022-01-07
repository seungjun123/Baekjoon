S = input().upper()
SS = list(set(S))

cnt_list = []
for i in SS:
    cnt = S.count(i)
    cnt_list.append(cnt)

if(cnt_list.count(max(cnt_list)) > 1):
    print("?")
else:
    print(SS[cnt_list.index(max(cnt_list))])