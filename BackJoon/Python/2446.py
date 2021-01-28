input_cnt = int(input())

for i in range(input_cnt, 0, -1) :
    print(' ' * (input_cnt - i) +  "*" * (2 * i - 1))
for j in range(2, input_cnt+1) :
    print(' ' * (input_cnt - j) + "*" * (2*j - 1))