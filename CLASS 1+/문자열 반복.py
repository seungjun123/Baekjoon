n = int(input())

for i in range(n):
    text = ""
    num, temp = input().split()
    num = int(num)
    for j in range(len(temp)):
        text += temp[j]*num
        
    print(text)