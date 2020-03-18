input_num = int(input())
max_num = []

for i in range(input_num) :
    max_num.append(int(input()))

max_num.sort()
for i in max_num :
    print(i)