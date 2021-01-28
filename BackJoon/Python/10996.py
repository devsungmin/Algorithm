input_num = int(input())
if input_num == 1:
    print('*')

else :
    for i in range(1, 2 * input_num + 1) :
        for j in range(1, input_num + 1) :
            if (i+j) % 2 == 0 :
                print("*", end = "")
            else :
                print(" ", end = "")

        print()