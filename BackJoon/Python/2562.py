cnt = 0
max = 0
tmp = 0

for i in range(1,10):
    num = int(input())
    if num > max :
        tmp =  num
        num = max
        max = tmp
        cnt = i

print('%d\n%d' %(max, cnt))