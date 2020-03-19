cnt = int(input())

for i in range(cnt) :
    num1, num2 = map(int,input().split(',')) # 콤마로 구분한다.
    print(num1+num2)