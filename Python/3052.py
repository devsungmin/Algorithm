remainder = [] # 42로 나눗값을 리스트 형식으로 하여 저장

for i in range(10) : # 10개를 입력 받아 진행함
    num = int(input())
    remainder.append(num % 42) # 42로 나눗값을 append를 사용하여 리스트에 추가함

remainder = set(remainder) # 교집합으로 같은 것끼리 묶음
print(len(remainder)) # 교집합으로 묶은 것을 길이로 하여 갯수를 표현함