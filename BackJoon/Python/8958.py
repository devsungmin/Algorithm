cnt = int(input())

for i in range(cnt) :
    list_num = list(input())
    sum_num = 0
    count = 1
    for j in list_num :
        if j == 'O' or j == 'o':
            sum_num += count
            count += 1
        else :
            count = 1
    print(sum_num)