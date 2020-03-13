# 대소문자를 구문해주는 문장을 만들기 위해서 upper() 함수를 사용함
input_str = str(input().upper())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
max_str = 0

for char in alpha:
    char_num = input_str.count(char)
    if char_num > max_str:
        char_maxnum = char_num

max_alpha = []
for char in alpha:
    if input_str.count(char) == char_maxnum:
        if max_alpha:
            max_alpha.append(char)
            print("?")
            break
        else:
            max_alpha.append(char)

if len(max_alpha) == 1:
    print(max_alpha[0])