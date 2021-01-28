s = str(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
list_str = []
str_num = []

# 입력 받은 단어를 list_str에 append를 이용해 list에 추가
for a in s :
    list_str.append(a)

# list에 있는 값들을 하나씩 비교하여 자리수의 값을 추가하고, 없을 경우 -1을 append 해줌
for i in alphabet :
    for j in range(len(list_str)) :
        if i == list_str[j] :
            str_num.append(j)
            break
        elif j < len(list_str)-1 :
            continue
        else :
            str_num.append(-1)

# 마지막에 공백을 넣어줌
for k in str_num :
    print(k,end=" ")