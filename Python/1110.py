# 이 문제는 연산의 나머지와 나눗셈을 이용한 문제이다.

num = int(input())
chk = num
new_sum = 0
sum_num = 0 # 26 일 경우 2+6을 더한 값
cnt = 0
while True:
    sum_num = num//10 + num%10 # 10의 자리와 1일 자리를 구분하여 덧셈 하는 수식
    new_sum = (num%10)*10 + sum_num%10 # sum_num에서 연산해서 나온값의 1의 자리와 덧셈을 하는 수식
    cnt += 1
    num = new_sum
    if new_sum == chk:
        break
print(cnt)