num1, num2 = input().split()

# 문자 거꾸로 정수형으로 저장
num1_reverse = int(num1[::-1])
num2_reverse = int(num2[::-1])

# 거꾸로 저장한 숫자중 큰 숫자 출력
max_num = max(num1_reverse, num2_reverse)
print(max_num)